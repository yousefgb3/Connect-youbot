import telebot

TOKEN = "8181550993:AAE-gB57Etk38TGJVe_Uuo6OwwgXXLbNocg"
bot = telebot.TeleBot(TOKEN)

OWNER_ID = 339450465

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "ربات با موفقیت راه‌اندازی شد!")
    else:
        bot.reply_to(message, "شما مجاز به استفاده از این ربات نیستید.")

bot.infinity_polling()
