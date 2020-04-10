# Перебор (итерирование) символов строки**********
name = "Тед"
for character in name:
    print(character)

# Перебор элементов списка**********
shows = ["Во все тяжкие",
        "Секретные материалы",
        "Фарго"]
for show in shows:
    print(show)

# Перебор ключей в словаре**********
people = {"Джим Парсонс":
          "Теория большого взрыва",
          "Брайан Крэнстон":
          "Во все тяжкие",
          "Екатерина Старшова":
          "Папины дочки"}
for character in people:
    print(character)

# Изменение элементов в изменяемом итерируемом объекте
tv = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
i = 0
for shown in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

# Синтаксис получения доступу к элементам объекта по его индексу
tv = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

# Перемещение данных между изменяемыми итерируемыми объектами
tv = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
coms = ["Теория большого взрыва",
        "Друзья",
        "Папины дочки"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

# Функция range**********
for i in range(1, 11):
    print(i)

# Циклы while**********
# Выполняет код, пока выражение истинно (True)
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print('C новым годом!')

# Бесконечный цикл**********
"""while True:
    print('Привет, МИР!')   # Можно выключить - Ctrl+C
"""

# Инструкция break**********
# Прекращает цикл
for i in range(0, 100):
    print(i)
    break

qs = ["Как тебя зовут? ",
      "Твой любимый цвет? ",
      "Что ты делаешь? "]
n = 0
while True:
    print("Введите X для выхода")
    a = input(qs[n])
    if a == 'X':
        break
    n = (n + 1) % 3
    #всегда, когда первое число в выражении с оператором деления по модулю меньше вто­рого. о-i вс ю.м является это первое число.

# Инструкция continue
# прекращает текущую итерацию цикла, и продолжает со следующей итерации
for i in range(1, 6):
    if i == 3:
        continue    # пропускаем i = 3
    print(i)

# Вложенные циклы
for i in range(1, 3):
    print(i)
    for letter in ("а", "б", "в"):
        print(letter)

# Пример:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

# Пример: цикл for внутри цикла while
while input('д или н?: ') != 'н':
    for i in range(1, 6):
        print(i)

# 1
list1 = ["Ходячие мертвецы",
         "Красавцы",
         "Клан сопрано",
         "Дневники вампира"]
for i in range(0, len(list1)):
    print(list1[i])

for show in list1:
    print(show)

# 2
for i in range(25, 51):
    print(i)

# 3
i = 0
for show in list1:
    print("{} {}".format(i, show))
    i += 1

for index, show in enumerate(list1):
    print(index)
    print(show)

# 4
numbers = [2, 7, 11, 19, 23, 27]
while True:
    a = input("Введите целое число или X для выхода: ")
    if a == "X":
        break
    try:
        a = int(a)
    except ValueError:
        print("Введите целое число или X для выхода")
    if a in numbers:
        print("Вы угадали!")
    else:
        print("Попробуйте еще раз!")

# 5
number1 = [8, 19, 148, 4]
number2 = [9, 1, 33, 83]
number = []
for i in number1:
    for j in number2:
        number.append(i * j)
print(number)

