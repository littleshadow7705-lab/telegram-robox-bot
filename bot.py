from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("TOKEN")

reply_map = {
    "k": "0",
    "e": "1",
    "y": "2",
    "b": "3",
    "o": "4",
    "r": "5",
    "d": "6",
    "1": "7",
    "2": "8",
    "3": "9",
    "f": "00",
    "g": "50"
}

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    result = ""

    for char in text:
        if char in reply_map:
            result += reply_map[char]

    if result:
        await update.message.reply_text(result)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()
