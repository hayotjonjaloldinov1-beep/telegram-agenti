import os
from dotenv import load_dotenv

# .env faylidan o'zgaruvchilarni yuklash
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def validate_config():
    """
    Sozlamalarni tekshirish funksiyasi.
    Agarda tokenlar o'rnatilmagan bo'lsa False qaytaradi.
    """
    is_valid = True
    if not TELEGRAM_BOT_TOKEN or TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        print("XATOLIK: .env faylida TELEGRAM_BOT_TOKEN kiritilmagan!")
        is_valid = False
    
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY_HERE":
        print("XATOLIK: .env faylida GEMINI_API_KEY kiritilmagan!")
        is_valid = False
        
    return is_valid
