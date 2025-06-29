import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN = "7898891497:AAHe2velplZq73bfMtEaKReIZoAWlsL6Vg"
ADMIN_ID = 5073544572
FREE_LIMIT = 3
user_queries = {}

logging.basicConfig(level=logging.INFO)

WELCOME_TEXT = """👋 Привет! Я OSINT Бот Ruslan’a.
🔍 Я могу:

📞 /phone +998901234567 – найти данные по номеру
📧 /email test@mail.com – проверить email
👤 /nick nickname – найти ник
🌐 /ip 8.8.8.8 – геолокация по IP
📱 /social +998... – соцсети по номеру

⚠️ 3 запроса бесплатно. Потом нужна подписка.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
