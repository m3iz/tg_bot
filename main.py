import telebot
import os
import g4f
import sys

from modules import shedul, backend, fetch, timer



g4f.debug.logging = False # Disenable logging
g4f.check_version = False # Disable automatic version checking
#245537285 chat id
#@kin0bunker - channel

# Здесь вы должны указать токен своего бота 
TOKEN = "964241877:AAGutKVF-Yake89PwsYmxsGLzq--yF4wi9s"
# Создайте объект бота
bot = telebot.TeleBot(TOKEN)

post_id = 1

def fetch_film():
    nfilm = fetch.Film()
    backend.insert_image(nfilm.get_poster(), "Title",nfilm.get_info())

def restart_script():
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours} час(а/ов), {minutes} минут(а/ы), {seconds} секунд(а/ы)"
def make_post():
    timer.timer.reset()
    fetch_film()
    global post_id
    try:
        image_record = backend.get_image(post_id)
        if image_record:
            image, title, description = image_record[1], image_record[2], image_record[3]
        post_id=post_id+1
        bot.send_photo("@kin0bunker", image, caption=image_record[3])
    except:
        post_id = 1
        image_record = backend.get_image(post_id)

        if image_record:
            image, title, description = image_record[1], image_record[2], image_record[3]
        post_id=post_id+1
        bot.send_photo("@kin0bunker", image, caption=image_record[3])
# Функция, которая вызывается при команде /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я многофункциональный бот.")

@bot.message_handler(commands=['fetch'])
def handle_fetch(message):
    bot.send_message(message.chat.id, "Ищем новый фильм и добавляем его в базу")
    fetch_film()

@bot.message_handler(commands=['stop'])
def handle_stop(message):
    bot.send_message(message.chat.id, "Останавливаю бота.")
    sys.exit()

@bot.message_handler(commands=['timer'])
def handle_timer(message):
    bot.send_message(message.chat.id, format_time(timer.timer.get_time()))
@bot.message_handler(commands=['post'])
def handle_post(message):
    bot.send_message(message.chat.id, "Пост сделан")
    make_post()
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
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": message.text}],
        )  # alternative model setting
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, "Something went wrong")
@bot.message_handler(commands=['dir'])
def handle_dir(message):
    file_list = os.listdir()
    result="Список файлов: "
    for file in file_list:
        result += file+ " "
    bot.send_message(message.chat.id, result)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "Вот что я умею:\n /restart - перезапуск бота\n /stop - выключить бота\n /dir - вывести список файлов на сервере\n /gpt 'request' - запрос в chatGPT\n /dbclear - очистить базу данных\n/dbshow - показать количество записей в базе данных\n")


@bot.message_handler(commands=['dbclear'])
def handle_dbclear(message):
    backend.delete_table_content()
    bot.send_message(message.chat.id, "Database cleared")

@bot.message_handler(commands=['rand'])
def handle_rand(message):
    nfilm = fetch.Film()
    bot.send_photo(message.chat.id, nfilm.get_poster(), nfilm.get_info())
@bot.message_handler(commands=['dbshow'])
def handle_dbshow(message):
    try:
        res = backend.view_table_content()
        bot.send_message(message.chat.id, res)
    except:
        print("Таблица пустая")
        bot.send_message(message.chat.id, "Таблица пустая")

# Функция, которая вызывается при отправке текстового сообщения
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я понимаю только команды: /rand - Посоветую фильмслучайного жанра\n/com - Помогу выбрать комедию\n/horr - Подберу ужастик\n/tril - Найду триллер")

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
    backend.insert_image(file_info, 'Title', message.caption)
    os.remove(file_name)
# Запускаем бота
if __name__ == "__main__":
    scheduler = shedul.schedul_init(make_post, 45)
    #backend.insert_image('toyota-supra.jpg', 'Title Here', 'Description Here')
    #backend.save_image_from_db(1, 'output_image.jpg')
    bot.polling()
    
