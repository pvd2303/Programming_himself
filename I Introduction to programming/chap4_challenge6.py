def squared(x):
    """Возведение числа в квадрат """
    return x ** 2

def mystr_new(s):
    """Вывод строки"""
    print(s)

def func(x, y, z, a = 10, b = "необязательный аргумент"):
    """Функция с тремя обязательными
    и двумя необязательными аргументами"""
    print(x, y, z, a, b)

def func1(x):
    return x / 2
def func2(y):
    return y * 4

def func1(s):
    """Обработка исключений"""
    try:
        return float(s)
    except ValueError:
        print("Неправильный ввод")

func(1, 2, 3, 100, "один")