from apscheduler.schedulers.background import BackgroundScheduler
import time

def update():
    """
    Ваша функция, которая должна выполняться каждые tcount секунд.
    """
    print("Функция update() вызвана.")

def schedul_init(func, tnum):

    # Создаем экземпляр планировщика
    scheduler = BackgroundScheduler()

    # Добавляем задачу на периодический вызов функции update каждый час
    scheduler.add_job(func, 'interval', minutes=tnum)

    # Запускаем планировщик в фоновом режиме
    scheduler.start()
    return scheduler

# Ваш основной код, например, запуск телеграм-бота
if __name__ == "__main__":
    scheduler = schedul_init(update)
    try:
        while True:
        # Здесь может быть ваш основной код
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
    # Останавливаем планировщик перед выходом из программы
        scheduler.shutdown()
