
import logging
import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Token dari environment (Railway)
TELEGRAM_TOKEN = os.getenv("OpenTELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Setup OpenAI API
openai.api_key = OPENAI_API_KEY

# Log
logging.basicConfig(level=logging.INFO)

# Command /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat datang ke GOLDROOT bot. Tanyakan apa saja...")

# Bila user mesej, jawab guna OpenAI
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    bot_reply = response.choices[0].message.content
    await update.message.reply_text(bot_reply)

# Run bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == '__main__':
    main()
