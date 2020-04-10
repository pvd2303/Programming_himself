def func(s):
    try:
        return float(s)
    except ValueError:
        print("Неправильный ввод")

string = "123.45"
print(func(string))

string = "строка"
print(func(string))
