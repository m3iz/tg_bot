import telebot
import os

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

# Функция, которая вызывается при отправке файла
@bot.message_handler(content_types=['document'])
def handle_document(message):
    # Получаем путь к текущей директории (где находится скрипт)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Устанавливаем текущую директорию
    os.chdir(current_dir)
    # Сохраняем файл
    file_info = bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)
    file_name = message.document.file_name
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)

# Запускаем бота
if __name__ == "__main__":
    bot.polling()
