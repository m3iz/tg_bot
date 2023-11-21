import sqlite3
import os

# Подключение к базе данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    image BLOB,
    title TEXT,
    description TEXT
)
''')
conn.commit()



def view_table_content():
    """
    Функция для просмотра содержимого таблицы 'images'.
    """
    cursor.execute("SELECT * FROM images")
    records = cursor.fetchall()
    for row in records:
        print(row)

def delete_table_content():
    """
    Функция для удаления содержимого таблицы 'images'.
    """
    cursor.execute("DELETE FROM images")
    conn.commit()
    print("Все записи удалены из таблицы 'images'.")

def insert_image(image_path, title, description):
    """
    Функция для вставки изображения и строк в базу данных.
    """
    with open(image_path, 'rb') as file:
        blob_data = file.read()
    
    cursor.execute("INSERT INTO images (image, title, description) VALUES (?, ?, ?)", 
                   (blob_data, title, description))
    conn.commit()

def get_image(image_id):
    """
    Функция для получения изображения и строк по ID.
    """
    cursor.execute("SELECT * FROM images WHERE id=?", (image_id,))
    record = cursor.fetchone()
    return record

def save_image_from_db(image_id, output_file):
    """
    Функция для извлечения изображения из базы данных и сохранения его в файл.

    Args:
    image_id (int): Идентификатор изображения в базе данных.
    output_file (str): Путь и имя файла, в который будет сохранено изображение.
    """
    # Выполнение запроса к базе данных для получения изображения
    cursor.execute("SELECT image FROM images WHERE id = ?", (image_id,))
    record = cursor.fetchone()

    if record:
        # Запись данных изображения в файл
        with open(output_file, 'wb') as file:
            file.write(record[0])
        print(f"Изображение сохранено в файл: {output_file}")
    else:
        print("Изображение с таким ID не найдено в базе данных.")
# Пример использования
insert_image('toyota-supra.jpg', 'Title Here', 'Description Here')
save_image_from_db(1, 'output_image.jpg')
image_record = get_image(1)



if image_record:
    image, title, description = image_record[1], image_record[2], image_record[3]
    with open('retrieved_image.jpg', 'wb') as file:
        file.write(image)
    print("Title:", title)
    print("Description:", description)

# Просмотр содержимого таблицы
view_table_content()

# Удаление содержимого таблицы
delete_table_content()
