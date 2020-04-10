# -*- coding: utf-8 -*-

# ФАЙЛЫ
# ЗАПИСЬ В ФАЙЛЫ**********
# Функция open
# Модуль os
import os
"""
Функция path этого модуля принимает в качестве
параметра каждую папку из пути к файлу и 
выстраивает вам правильный путь к файлу.
Доп.информация здесь: 
theselftaughtprogrammer.io/filepaths
"""
print(os.path.join("Users",
                   "bob",
                   "st.txt"))

"""
Режимы открытия файло функции open:
"г" — открывает файл только для чтения.
"w" — открывает файл только для записи. 
    Удаляет содержимое файла, если файл 
    существует; если файл не существует, 
    создает новый файл дія записи.
"W+" — открывает файл дія чтения и записи. 
    Удаляет содержимое файла. если 
    файл существует; если файл не существует, 
    создает новый файл дія чтения и записи*.
open - эта функция создает новый файл, 
    если он не существует
write - этот метод функции open 
    производит запись в файл
close - этот метод функции open 
    производит закрытие файла
"""
st = open("st.txt", "w")
st.write("Привет от Python")
st.close()

# Автоматическое закрытие файлов**********
# Инструкция with
with open("st.txt", "w") as f:
    f.write("привет от Python!")

# Чтение файлов***********
# Метод read
my_list = list()

with open("st.txt", "r") as f:
    my_list.append(f.read())
    #print(f.read()) - метод read не закрывая и не открывая файл можно только
    #  один раз

print(my_list)

# CSV-файлы***********
"""
CSV-файл имеет расширение .csv и содержит данные,
    разделенные c помощью запятых 
    (CSV расшифровывается как Comma Separated Values 
    — значения, разделенные запятыми)
"""
"""
модуль csv в инструкции with
csv.writer - принимает файловый объект и разделитель
csv.writerow - этот метод создает только одну строку
"""
import csv
with open("st.csv", "w") as f:
    w = csv.writer(f,
                   delimiter = ",")
    w.writerow(["один",
               "два",
               "три"])
    w.writerow(["четыре",
                "пять",
                "шесть"])

with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter = ",")
    for row in r:
        print(",".join(row))
"""
При каждом прохождении цикла вы вызываете метод
join в занятой, чтобы добавить запятую между
каждым фрагментом данных в файле, и выводите 
содержимое так, как оно выглядит в исходном файле (с разделяющи­ми запятыми).
"""

#1
"""
Для вывода русских символов в консоль после чтения
файла - добавить в open: encoding="utf8" 
как в примере ниже
"""
my_list = list()
with open("Модули.py", "r", encoding="utf8") as f:
    my_list.append(f.read())
print(my_list)

#2
answer = input("Как Вас зовут: ")
with open("Challenge2.txt", "w") as f:
    f.write(answer)
answer = ""
with open("Challenge2.txt", "r") as f:
    answer = f.read()
print(answer)

my_list = []
answer = input("Как Вас зовут: ")
with open("Challenge2.txt", "w") as f:
    f.write(answer)

with open("Challenge2.txt", "r") as f:
    my_list.append(f.read())
print(my_list)

#3
import csv

films = [["Звездные войны",
          "Терминатор",
          "Искусственный интелект"],
         ["Дурак",
          "Матильда",
          "Левиафан"],
         ["Люди в черном",
          "Я - робот",
          "Эволюция"]]
with open("challenge3.csv", "w") as f:
    w = csv.writer(f,
                   delimiter=",")
    for lst in films:
        w.writerow(lst)

