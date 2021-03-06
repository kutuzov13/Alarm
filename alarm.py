import time
import os
import threading


class Alarm(threading.Thread):
    def __init__(self, hours, minutes):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.keep_running = True

    def run(self):
        try:
            while self.keep_running:
                now = time.localtime()
                if now.tm_hour == self.hours and now.tm_min == self.minutes:
                    time.localtime()
                    print('Alarm!!!')
                    os.startfile(r'The Weeknd - False Alarm.mp3')
                    return
        except:
            return

    def just_die(self):
        self.keep_running = False


name = input('Enter your name: ')
print(f'Hello {name}')

alarm_HH = input("Enter the hour you want to wake up: ")
alarm_MM = input("Enter the minute you want to wake up: ")
print(f'You wanted to wake up in {alarm_HH}:{alarm_MM}')

alarm = Alarm(alarm_HH, alarm_MM)
alarm.run()
