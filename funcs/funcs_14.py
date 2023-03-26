# Описать функцию fact2( n ), вычисляющую двойной факториал :n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n, если n — четное.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел
def factorial(n: int) -> int:
    result = 1
    for i in range((1 if n % 2 else 2), n + 1, 2):
        result *= i
    return result

def main():
    print(factorial(5))
if __name__ == '__main__':
    main()

