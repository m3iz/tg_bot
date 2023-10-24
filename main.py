import telebot

# Здесь вы должны указать токен своего бота
TOKEN = "964241877:AAGutKVF-Yake89PwsYmxsGLzq--yF4wi9s"

# Создайте объект бота
bot = telebot.TeleBot(TOKEN)

# Функция, которая вызывается при команде /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш бот.")

# Функция, которая вызывается при отправке текстового сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Запускаем бота
if __name__ == "__main__":
    bot.polling()
