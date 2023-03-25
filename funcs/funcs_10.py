# Написать функцию по решению квадратных уравнений.
def SquareRoot(func, a, b, c) -> int:
    D = func(a, b, c)
    if D < 0:
        return []
    else:
        x1 = (-b - ((b * b - 4 * a * c) ** 0.5))/(2 * a)
        x2 = (-b + ((b * b - 4 * a * c) ** 0.5))/(2 * a)
    return [x1, x2]

def Discr(a, b, c):
    return b * b - 4 * a * c

def main():
    roots = SquareRoot(Discr, 5, 4, -1)
    if roots != []:
        print("x1 = ", roots[0])
        print("x2 = ", roots[1])
    else:
        print("The end")
if __name__ == '__main__':
    main()
