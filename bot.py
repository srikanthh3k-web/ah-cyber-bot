from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8988866569:AAHbtvNVWdMkhEDU-JaALGROIx2Q-JLCto0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛡 VAPT ₹999", callback_data="vapt")],
        [InlineKeyboardButton("🐧 Linux ₹499", callback_data="linux")],
        [InlineKeyboardButton("💻 Python ₹699", callback_data="python")],
        [InlineKeyboardButton("🌐 Web Hacking ₹799", callback_data="web")]
    ]

    await update.message.reply_text(
        "🔥 AH Cyber Solutions 🔥\n\nSelect Course 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
