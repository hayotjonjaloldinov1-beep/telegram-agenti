# 🤖 Jaloldinov Telegram Bot Agent

Bu loyiha **Jaloldinov** sahifasi uchun shaxsiy Telegram bot agentidir. Bot Google Gemini AI yordamida foydalanuvchilar bilan o'zbek tilida muloqot qiladi.

## ✨ Xususiyatlar

- 🧠 Google Gemini 1.5 Flash AI yordamida aqlli javoblar
- 💬 Har bir foydalanuvchi uchun alohida suhbat tarixi (xotira)
- 🇺🇿 O'zbek tilida muloqot
- 🕵️ Bot ekanligini tan olmaydi - "Ali" nomi bilan javob beradi
- ⚡ Tezkor va real-time javoblar

## 🚀 O'rnatish

### 1. Repositoriyani klonlash
```bash
git clone https://github.com/YOUR_USERNAME/telegram-agenti.git
cd telegram-agenti
```

### 2. Kerakli kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Muhit o'zgaruvchilarini sozlash
```bash
cp .env.example .env
```
`.env` faylini oching va quyidagilarni to'ldiring:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Botni ishga tushirish
```bash
python bot.py
```

## ☁️ Railway'ga Deploy Qilish

1. [Railway.app](https://railway.app) saytiga kiring
2. **New Project** → **Deploy from GitHub repo** tanlang
3. Bu repositoriyani tanlang
4. **Variables** bo'limiga kirip quyidagilarni kiriting:
   - `TELEGRAM_BOT_TOKEN` = sizning bot tokeningiz
   - `GEMINI_API_KEY` = sizning Gemini API kalitingiz
5. Deploy tugmasini bosing ✅

## 🔑 Kerakli API Kalitlar

| Kalit | Qayerdan olish |
|-------|---------------|
| `TELEGRAM_BOT_TOKEN` | [@BotFather](https://t.me/BotFather) orqali |
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/app/apikey) orqali |

## 📁 Fayl Tuzilmasi

```
telegram-agenti/
├── bot.py          # Asosiy bot kodi
├── config.py       # Sozlamalar va konfiguratsiya
├── requirements.txt # Python kutubxonalari
├── Procfile        # Railway/Heroku uchun
├── runtime.txt     # Python versiyasi
├── .env.example    # Muhit o'zgaruvchilari namunasi
└── README.md       # Bu fayl
```

## ⚠️ Muhim

- `.env` faylini **hech qachon** GitHub'ga yuklmang - unda maxfiy tokenlar mavjud!
- `.gitignore` fayli `.env` ni avtomatik himoya qiladi

## 📝 Litsenziya

MIT License
