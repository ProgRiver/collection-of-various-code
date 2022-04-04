
def join_sorted_lists(lst1, lst2):
    """Слияние двух сортированных списков"""
    result = []
    pointer1 = 0
    pointer2 = 0

    while pointer1 < len(lst1) and pointer2 < len(lst2):  # пока не закончился хотя бы один список
        if lst1[pointer1] <= lst2[pointer2]:
            result.append(lst1[pointer1])
            pointer1 += 1
        else:
            result.append(lst2[pointer2])
            pointer2 += 1

    if pointer1 < len(lst1):   # добавить остаток
        result += lst1[pointer1:]
    if pointer2 < len(lst2):
        result += lst2[pointer2:]
    
    return result


number_of_lists = int(input())
start_list = []

for _ in range(number_of_lists):
    lst_in = [int(j) for j in input().split()]  # ввод через пробел
    start_list = join_sorted_lists(start_list, lst_in)

print(*start_list)