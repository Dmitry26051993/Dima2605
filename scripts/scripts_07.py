# Написать скрипт - таймер. Создать программу Pomodoro.
# На вход программа получает имя, фамилию, время для фокусировки(по-умолчанию 25 минут),
# длину перерыва(по-умолчанию 5 минут), количество циклов(по-умолчанию 4) и название задачи.
# Программа указывает оставшееся время фокусировки, после сигнализирует о наступлении перерыва,
# после сигнализирует о начале нового цикла фокусировки.
# Программа должна вести файл лога о всех запусках.
import csv
import os
import time
from datetime import timedelta
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name')
parser.add_argument('-ln', '--last_name')
parser.add_argument('-m', '--min', type=int, default=25)
parser.add_argument('-br', '--break_time', type=int, default=5)
parser.add_argument('-c', '--cycles', type=int, default=4)
parser.add_argument('-t', '--task')

args = parser.parse_args()
time_start = time.ctime()

if not os.path.exists('longer.csv'):
    with open('log_timer.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        fields = ['first name', 'last name', 'time start', 'task']
        csvwriter.writerow(fields)

with open('longer.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    arr = [args.first_name, args.last_name, time_start, args.task]
    csvwriter.writerow(arr)


def cycle(kind, time_to):
    min = timedelta(minutes=1)
    delta_time = timedelta(minutes=time_to)
    print(f'start {kind}')
    while delta_time > timedelta():
        print(f'to the end of {kind} - {delta_time}')
        delta_time -= min
        time.sleep(60)
    print(f'end of {kind}')


for i in range(1, args.cycles + 1):
    print(f'cycle - {i}')
    cycle('concentrate', args.minutes)
    cycle('break', args.break_time)
print("Die")