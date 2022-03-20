# Задача Иосифа Флавия


def get_last_number(numbers=1, removed=1):
    """Функция определяет номер участника, который останется"""
    if numbers == 1:
        return 1
    else:
        return (get_last_number(numbers - 1, removed) + removed - 1) % numbers + 1


number_of_persons = int(input("Количество человек в кругу: "))
removed = int(input("Номер, который выбывает: "))

last_number = get_last_number(number_of_persons, removed)
print(last_number)
