# Сортировка выбором

def get_min_element(array: list) -> int:
    """функция для поиска наименьшего элемента в списке.
    """
    min_element = array[0]  # для наименьшего значения
    indx_min = 0            # для индекса наименьшего значения

    for i in range(1, len(array)):
        if array[i] < min_element:
            min_element = array[i]
            indx_min = i
    
    return indx_min


def sel_sort(lst: list) -> list:
    """функция сортировки выбором"""
    new_lst = []
    for _ in range(len(lst)):
        indx_min = get_min_element(lst)
        new_lst.append(lst.pop(indx_min))
    return new_lst


print(sel_sort([5, 3, 6, 2, 10, 8, 11, 1, 0, 15]))
