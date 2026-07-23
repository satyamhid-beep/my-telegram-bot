import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from google import genai

# -------------------------------------------------------------
# यहाँ अपनी Keys डालो (उद्धरण चिन्ह " " के अंदर)
TELEGRAM_BOT_TOKEN = "8781016869:AAFEMFA61mnmvUtgzWWt37mIEuVuiRGF70I"
GEMINI_API_KEY = "AQ.Ab8RN6LNSX5Gv1hjLQc5R4nzL13MPglNqsoTaHqNOgqmzHnvcQ"
# -------------------------------------------------------------

# Gemini Client सेटअप
client = genai.Client(api_key=GEMINI_API_KEY)

# /start कमांड का जवाब
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! मैं आपका AI असिस्टेंट हूँ। आप मुझसे कोई भी सवाल पूछ सकते हैं!")

# जब यूज़र मैसेज भेजे तो Gemini AI से जवाब लाकर देना
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_text,
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("क्षमा करें, जवाब देने में कोई समस्या आई। कृपया थोड़ी देर बाद प्रयास करें।")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot starting...")
    app.run_polling()
