import telebot
import os
import g4f
import sys

g4f.debug.logging = False # Disenable logging
g4f.check_version = False # Disable automatic version checking

# Здесь вы должны указать токен своего бота 
TOKEN = "964241877:AAGutKVF-Yake89PwsYmxsGLzq--yF4wi9s"
# Создайте объект бота
bot = telebot.TeleBot(TOKEN)

def restart_script():
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)

# Функция, которая вызывается при команде /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я многофункциональный бот.")

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.chat.id, "Останавливаю бота.")
    sys.exit()

@bot.message_handler(commands=['restart'])
def handle_restart(message):
    bot.send_message(message.chat.id, "Перезапускаю скрипт.")
    restart_script()

@bot.message_handler(commands=['gpt'])
def handle_gpt(message):
    # Открываем файл в режиме 'a' для добавления данных в конец файла
    with open('access.log', 'a') as file:
        file.write(message.text)
    file.close
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message.text}],
    )  # alternative model setting
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['dir'])
def handle_dir(message):
    file_list = os.listdir()
    result="Список файлов: "
    for file in file_list:
        result += file+ " "
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Вот что я умею:\n /restart - перезапуск бота\n /stop - выключить бота\n /dir - вывести список файлов на сервере\n /gpt 'request' - запрос в chatGPT\n")

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
    bot.reply_to(message, "Ваш файл получен и загружен на сервер")
# Запускаем бота
if __name__ == "__main__":
    bot.polling()
