from apscheduler.schedulers.background import BackgroundScheduler
import time

def update():
    """
    Ваша функция, которая должна выполняться каждые tcount секунд.
    """
    print("Функция update() вызвана.")

# Создаем экземпляр планировщика
scheduler = BackgroundScheduler()

# Добавляем задачу на периодический вызов функции update каждый час
scheduler.add_job(update, 'interval', hours=1)

# Запускаем планировщик в фоновом режиме
scheduler.start()

# Ваш основной код, например, запуск телеграм-бота
try:
    while True:
        # Здесь может быть ваш основной код
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    # Останавливаем планировщик перед выходом из программы
    scheduler.shutdown()
