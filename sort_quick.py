# Быстрая сортировка.

def get_quick_sort(lst):
    """Рекурсивная функция. Быстрая сортировка."""
    if len(lst) < 2:
        return lst
    else:
        # опорный средний элемент списка
        support_element = lst[0]
        sp_min = [i for i in lst[1:] if i <= support_element]
        sp_max = [i for i in lst[1:] if i > support_element]
        return get_quick_sort(sp_min) + [support_element] + get_quick_sort(sp_max)


lst_in = [-1, 5, 3, 6, 2, 10, 8, 11, 1, 0, 15, 33, 50, 100, -4, 77, 25]
print(get_quick_sort(lst_in))
