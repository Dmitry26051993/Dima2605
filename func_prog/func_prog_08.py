# Написать декоратор, который будет выводить время выполнения функции
# from datetime import datetime
# time = datetime.now()
from datetime import datetime
def ineer(*args, **kwargs):
    start_time = datetime.now()
    result = func(*args, **kwargs)
    finish_time = datetime.now()
    delta = finish_time - start_time
    print(delta)
    return result

def very_importnant_func(arr):
    arr = list(map(lambda x: x * 2, arr))
    print(arr)
    return arr
arr = [i for i in range(10)]
very_importnant_func(arr)