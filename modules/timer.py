import threading
import time

class TimerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._time = 0
        self._running = True

    def run(self):
        while self._running:
            time.sleep(1)
            self._time += 1
            #print(timer.get_time())

    def stop(self):
        self._running = False

    def get_time(self):
        return self._time

    def reset(self):
        self._time = 0

# Создание и запуск таймера
timer = TimerThread()
timer.start()

timer.reset()

    # Продолжение работы после сброса

timer.get_time()

