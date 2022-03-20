from math import factorial


def pascal_triangle(number: int) -> list:
    """Функция расчета треугольника Паскаля"""
    main_list = []
    for j in range(number):
        lists_nested = []
        for i in range(j + 1):
            lists_nested.append(int(factorial(j) / (factorial(i) * factorial(j - i))))
        main_list.append(lists_nested)
    return main_list


num = int(input("Ввести высоту треугольника: "))
print(*pascal_triangle(num), sep='\n')
