# Создать список поездов.
# Структура словаря: номер поезда, пункт и время прибытия, пункт и время отбытия.
from datetime import timedelta
trains = [
    {
        'number': 768,
        'depart': 'Vitebsk',
        'depart_time': [5, 2],
        'destin': 'Grodno',
        'destin_time': [11, 13]
    },
    {
        'number': 152,
        'depart': 'Minsk',
        'depart_time': [1, 35],
        'destin': 'Gomel',
        'destin_time': [10, 39]
    },
    {
        'number': 72,
        'depart': 'Minsk',
        'depart_time': [0, 26],
        'destin': 'Brest',
        'destin_time': [5, 1]
    }
]
# Вывести все сведения о поездах, время пребывания в пути которых превышает 7 часов 20 минут.
long_distance_trains = []
time_limit = timedelta(hours=7, minutes=20)
for train in trains:
    for key, v in train.items():
        if key == 'depart_time':
            dep = v
        elif key == 'destin_time':
            dest = v
            diff = timedelta(hours=dest[0], minutes=dest[1]) - timedelta(hours=dep[0], minutes=dep[1])
    if diff > time_limit:
        long_distance_trains.append(train)
print(long_distance_trains)
# Примечание:
# данное задание подразумевает самостоятельное изучение принципов работы со временем в Python(библиотека datetime)

