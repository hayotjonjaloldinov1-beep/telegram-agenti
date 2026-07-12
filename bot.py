import telebot
import google.generativeai as genai
import config
from flask import Flask
import threading
import os

# Dummy Web Server (Render uchun port band qilish)
app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram Bot is running!"

def run_server():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Konfiguratsiyani tekshirish
if not config.validate_config():
    print("Xato: Botni ishga tushirish uchun .env faylini to'ldiring!")
    exit(1)

# Telegram Bot va Gemini API'ni sozlash
bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)
genai.configure(api_key=config.GEMINI_API_KEY)

# Tizimli ko'rsatma (System Instruction)
system_instruction = (
    "Sening isming Ali. Sen 'Jaloldinov' sahifasi/profili egasining shaxsiy yordamchisisan. "
    "Foydalanuvchilar bilan doim samimiy, xuddi insondek va qisqa (1 yoki maksimal 2 ta gap bilan) muloqot qilasan. "
    "Mijozlar/obunachilar bilan o'zbek tilida gaplash. "
    "Agar sendan 'botmisan?', 'sun'iy intellektmisan?' yoki shunga o'xshash savol so'rashsa, "
    "aniq qilib: 'Yo'q, man Aliman shu profil egasini yordamchisiman' deb javob ber. Hech qachon bot yoki robot ekanligingni tan olma."
)

# Gemini modelini sozlash
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_instruction
)

# Har bir chat_id uchun alohida chat tarixi (memory) saqlash
user_chats = {}

def get_user_chat(chat_id):
    if chat_id not in user_chats:
        user_chats[chat_id] = model.start_chat(history=[])
    return user_chats[chat_id]

def is_asking_if_bot(text):
    """
    Foydalanuvchi bot yoki sun'iy intellekt ekanligimiz haqida so'rayotganini tekshirish.
    """
    text_lower = text.lower().strip()
    bot_keywords = [
        "botmisan", "botmi", "robotmi", "robotmisan", 
        "bot san", "botsan", "bot-misan", "ai-misan", 
        "sun'iy intellekt", "suniy intellekt", "chatgpt"
    ]
    return any(keyword in text_lower for keyword in bot_keywords)

# /start komandasi uchun handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name or "do'stim"
    
    # Har bir yangi startda chat tarixini tozalash yoki yangilash mumkin
    user_chats[chat_id] = model.start_chat(history=[])
    
    welcome_text = f"Assalomu alaykum, {first_name}! Men Aliman, 'Jaloldinov' sahifasi egasining yordamchisiman. Sizga qanday yordam bera olaman? 😊"
    bot.reply_to(message, welcome_text)

# Oddiy matnli xabarlar uchun handler
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    chat_id = message.chat.id
    user_text = message.text
    
    # Qattiq talabni tekshirish: Botmisan deb so'ralsa
    if is_asking_if_bot(user_text):
        bot.reply_to(message, "Yo'q, man Aliman shu profil egasini yordamchisiman")
        return
        
    try:
        # User session chatini olish va xabarni yuborish
        chat = get_user_chat(chat_id)
        
        # Bot nomidan yozilayotganini bildirish uchun 'typing' statusini ko'rsatish
        bot.send_chat_action(chat_id, 'typing')
        
        response = chat.send_message(user_text)
        reply_text = response.text.strip()
        
        # Javobni qaytarish
        bot.reply_to(message, reply_text)
        
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        bot.reply_to(message, "Kechirasiz, hozir javob bera olmayman. Birozdan so'ng qayta urinib ko'ring.")

if __name__ == '__main__':
    print("Jaloldinov Telegram Bot Agent ishga tushmoqda...")
    
    # Web serverni orqa fonda ishga tushirish (Render xatoligini to'g'rilash uchun)
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

    try:
        # Webhook konfliktlarini o'chirish
        bot.remove_webhook()
    except Exception as e:
        print(f"Webhook o'chirishda xatolik: {e}")
    
    # Botni doimiy eshitish rejimida yoqish
    bot.infinity_polling()
