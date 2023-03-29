# Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
from datetime import datetime
from random import randint

def measure_time(func):
    def ineer(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        finish_time = datetime.now()
        delta = finish_time - start_time
        print(delta)
        return result
    return ineer


@measure_time
def very_importnant_func(arr):
    arr = list(map(lambda x: x * 2, arr))
    print(arr)
    return arr
arr = [randint(-100, 1000) for i in range(1000)]
very_importnant_func(arr)



