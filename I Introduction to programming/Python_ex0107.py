# Отработка исключений
try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("ошибка ввода")