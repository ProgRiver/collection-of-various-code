
def binary_search(list_in: list, key: int):
    """Бинарный поиск элемента в сортированном списке.
    """
    first = 0
    end = len(list_in) - 1

    while first <= end:
        centr = (first + end) // 2
        if list_in[centr] == key:
            return f"Индекс искомого элемента: {centr}"
        elif list_in[centr] > key:
            end = centr - 1
        elif list_in[centr] < key:
            first = centr + 1
    
    return "Элемента нет в списке"


nums = [1, 2, 5, 6, 8, 10, 12, 15, 17, 20]
print(binary_search(nums, 5))
