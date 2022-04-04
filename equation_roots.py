# Вещественные корни уравнения

from math import sqrt

a, b, c = [float(input()) for i in range(3)]

D = b**2 - 4 * a * c

if D < 0:
    print("Нет корней")
elif D == 0:
    print(-(b / (2 * a)))
elif D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')