from random import choice


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
sumb = "il1Lo0O"  #набор символов для исключения из пароля


def controls(string):
    """Функция проверки ответа"""
    while string not in ("да", "нет"):
        string = input("[!] Введите 'да' или 'нет'... ")
    return string


def control_numb(num):
    """Функция проверки на целое положительное число != 0"""
    while not num.isdigit() or int(num) <= 0:
        num = input("[!] Введите целое число больше нуля... ")
    return num


def get_delete(st_chars, answer_s5):
    """Функция удаление/неудаление символов, указанных в переменной 'sumb'"""
    if answer_s5 == "нет":
        return st_chars
    else:
        for s in sumb:
            st_chars = st_chars.replace(s, "")
        return st_chars


def requests():
    """Функция формирования символов для передачи в генератор паролей"""
    chars = ""
    s1 = controls(input("Содержит цифры? (да/нет) "))
    chars += digits if s1 == "да" else ""
    s2 = controls(input("Содержит прописные буквы? (да/нет) "))
    chars += uppercase_letters if s2 == "да" else ""
    s3 = controls(input("Содержит строчные буквы? (да/нет) "))
    chars += lowercase_letters if s3 == "да" else ""
    s4 = controls(input("Содержит спецсимволы? (да/нет) "))
    chars += punctuation if s4 == "да" else ""
    s5 = controls(input(f"Исключать символы {sumb} ? (да/нет) "))
    chars = get_delete(chars, s5)
    return chars


def generate_password(len_pas, total_string):
    """Функция генератор пароля"""
    password = ""
    for _ in range(int(len_pas)):
        password += choice(total_string)
    return password


# длина и количество не ограничены (предложение диапазона)
amount = control_numb(input("Количество паролей? (одно целое число от 1 до 5) "))
len_pas = control_numb(input("Длина пароля? (одно целое число от 9 до 12) "))
total_string = requests()

lst_pas = ["Список паролей: "]
for _ in range(int(amount)):
    lst_pas.append(generate_password(len_pas, total_string))
print(*lst_pas, sep='\n')
