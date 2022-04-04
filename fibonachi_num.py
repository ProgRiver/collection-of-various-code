
def numbers_fib(number):
    lst_num = [1, 1]
    if number == 1:
        return 1
    for i in range(2, number):
        lst_num.append(lst_num[i - 1] + lst_num[i - 2])
    return lst_num


number = int(input())
print(numbers_fib(number))