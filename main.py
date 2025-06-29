from telegram import Bot
from telegram.ext import Updater, CommandHandler

# Replace with your real Bot Token and User ID
BOT_TOKEN = "8074466998:AAFXP2YxBtWWYnMurQ3ikNNHzkpgsD7sQls"
OWNER_ID = 6240404116

def start(update, context):
    if update.effective_user.id == OWNER_ID:
        update.message.reply_text("🟢 Sudarshan Bot is now Active!")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
