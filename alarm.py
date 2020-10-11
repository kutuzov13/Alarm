import time
import os
import threading

class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):
                    time.localtime()
                    print('Вставаааай!!!')
                    os.startfile('путь к файлу формата .mp3')
                    return
        except:
            return

    def just_die(self):
        self.keep_running = False

name = input('Введите ваше имя: ')
print(f'Привет {name}')

alarm_HH = input("Введите час, в который вы хотите проснуться: ")
alarm_MM = input("Введите минуту, в который вы хотите проснуться: ")
print(f'Вы захотели проснуться в {alarm_HH}:{alarm_MM}')

alarm = Alarm(alarm_HH, alarm_MM)
alarm.run()
