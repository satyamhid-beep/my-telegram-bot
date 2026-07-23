
import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --------------------------------------------------
# आपकी Keys (Token और API Key)
# --------------------------------------------------
TELEGRAM_BOT_TOKEN = "8781016869:AAFEMFA61mnmVUtgzWWt37mIEuVuiRGF7OI"
GEMINI_API_KEY = "AQ.Ab8RN6LNSX5Gv1hjLQc5R4nzL13MPglNqsoTaHqNOgqmzHnvcQ"
# --------------------------------------------------

# Gemini AI सेटअप
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# /start कमांड का जवाब
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! मैं आपका AI असिस्टेंट हूँ। आप मुझसे कोई भी सवाल पूछ सकते हैं!")

# यूजर के मैसेज का जवाब (Gemini AI से)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = model.generate_content(user_text)
        await update.message.reply_text(response.text)
    except Exception as e:
        await update.message.reply_text("माफ़ करना, उत्तर देने में कोई समस्या आई है। कृपया थोड़ी देर बाद प्रयास करें।")

# मुख्य प्रोग्राम
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("Bot is running...")
    app.run_polling()
