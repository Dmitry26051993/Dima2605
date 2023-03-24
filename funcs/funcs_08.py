# Написать функцию принимающая на вход неопределенным количеством аргументов
# и именованный аргумент mean_type. В зависимости от mean_type вернуть среднеарифметическое
# либо среднегеометрическое.
# Написать программу в виде трех функций.
def avg(*args):
    avgs = sum(args) / len(args)
    return avgs
def avg_geom(*args):
    result = 1
    for i in args:
        result *= i
    return result ** (1 / len(args))

def result_avg(*args, mean_type):
    if mean_type == 1:
        return avg_geom(*args)
    if mean_type == 0:
        return avg(*args)
def main():
    print(f"sred geom - {result_avg(1, 2, 4, mean_type = 1)}")
    print(f"sred arif - {result_avg(1, 2, 4, mean_type = 0)}")
if __name__ == '__main__':
    main()
