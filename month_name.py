
def get_month(language="", number=""):
    """Определить название месяца на нужноя языке"""

    if language not in ('ru', 'en') or number not in range(1, 13):
        return "Ошибка ввода"

    months_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 
                 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    months_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
                 'august', 'september', 'october', 'november', 'december']
    
    if language == 'ru':
        return months_ru[number-1].title()
    elif language == 'en':
        return months_en[number-1].title()


lang = input("Enter language: ")
numb = int(input("Enter number month: "))
print(get_month(lang, numb))