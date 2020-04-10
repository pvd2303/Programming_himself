# ОБЪЕКТНО_ОРИЕНТИРОВАНИЕ ПРОГРАММИРОВАНИЕ
# КЛАССЫ**********
"""
Названия классов всегда начинаються с прописной
буквы в "горбатом" режиме и без символа подчеркивания
К примеру: LikeThis
"""

# МЕТОДЫ**********
"""
Название методов как и функций указываются строчными 
буквами и слова разделяются символом подчеркивания
"""

"""
По соглашению, первый параметр метода всегда называется
self. 
"""
class Orange:
    def __init__(self, w, c):
        self.weight = w     # переменная экземпляра, w - значение переменной
        self.color = c      # переменная экземпляра, c - значение переменной
        print("Создано!")

# Создание экземпляра класса - объекта класса
or1 = Orange(10, "темный апельсин")
print(or1)

print("=====", "\n")
# Получение значения переменных экземпляра:
print(or1.weight)
print(or1.color)

# Значение переменных экземпляра можно изменить:
or1.weight = 100
or1.color = "светлый апельсин"

print(or1.weight)
print(or1.color)

print("=====", "\n")
class Orange1:
    def __init__(self, w, c):
        """вес в граммах"""
        self.weight = w     # переменная экземпляра, w - значение переменной
        self.color = c      # переменная экземпляра, c - значение переменной
        self.mold = 0
        print("Создано!")

    def rot(self, days, temp):  # метод класса
        self.mold = days * temp

orange = Orange1(6, "апельсин")
print(orange.mold)
orange.rot(10,33)
print(orange.mold)

print("=====", "\n")

# В классе можно определять множество методов
# Пример построения модели прямоугольника
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

print("=====", "\n")

#Практикум к главе 12
#1
class Apple:
    def __init__(self, w, c, d, f):
        self.weight = w
        self.color = c
        self.dimention = d
        self.form = f

#2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

c1 = Circle(10)
print(c1.area())

print("=====", "\n")

#3
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def triangle_area(self):
        return self.width * self.height / 2

t1 = Triangle(10, 15)
print(t1.triangle_area())

print("=====", "\n")

#4
class Hexagon:
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def hex_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

h1 = Hexagon(1, 2, 3, 4, 5, 6)
print(h1.hex_perimeter())

print("=====", "\n")

# глава 13 Четыре главные концепции ООП:**********
# инкапсуляция, абстракция, полиформизм и наследование**********

# ИНКАПСУЛЯЦИЯ**********
# Инкапсуляция предотвращает прямой доступ извне к данным класса
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

#Два способа изменения данных внутри класса
#1-ый - напрямую в переменной nums
data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)
#2-ой - при помощи метода change_data
data_two = Data()
data_two.change_data(1, 200)
print(data_two.nums)

print("=====", "\n")

# В Python все переменные открытые
# Переменная или метод, к которым вызывающий
# не должен получить доступ, перед их именами
# нужно добавить нижнее подчеркивание "_"

class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self._unsafe = "опасно"

    def public_method(self):
        # Клиенты могут это использовать
        pass

    def _unsafe_method(self):
        # Клиенты не должны это использовать
        pass
        self.public = "безопасно"
        self._unsafe = "опасно"

# АБСТРАКЦИЯ **********
"""
При создании класса некоторые характеристики
урезаются до основных характеристик,
необходимых для решения конкретной задачи
"""
# ПОЛИФОРМИЗМ **********
"""
Полиморфизмом называют «способность 
(в программировании) представлять один 
и тот же интерфейс для разных 
базовых форм (типов данных).
Интерфейс — это функция или метод.
"""

"""
Примером полиформизма к примеру:
функция print - печатает любой объект,
независимо отего типа: int или string или float и тд
"""

# НАСЛЕДОВАНИЕ**********
"""
Класс может наследовать методы и переменные 
от другого класса. Класс, от которого наследуют, 
называется родительским, а класс, который наследует, 
дочерним 
"""

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {}""".
              format(self.width,
                   self.len))

my_shape = Shape(20, 25)
my_shape.print_size()

class Square(Shape):
    def area(self):
        return self.width * self.len

a_square = Square(20,20)
a_square.print_size()
print(a_square.area())

print("=====", "\n")

# Переопределение метода родительского класса
class Square1(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):       # переопределение
        print("""Я {} на {}""".
              format(self.width,
                   self.len))

a_square = Square1(20,20)
a_square.print_size()

print("=====", "\n")

# КОМПОЗИЦИЯ**********
"""
Композиция создает отношение "имеет", сохраняя
объект в другом объекте как переменную. 
Например, композиция может использоваться 
для представления отношения между собакой 
и ее хозяином (собака имеет хозяина). 
"""
class Dog:
    def __init__(self,
                 name,
                 breed,
                 owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

"""
Затем, когда вы создаете объект Dog, 
то передаете объект Person в качестве 
параметра - хозяина.
"""
mick = Person("Мик Джаггер")
stan = Dog("Стенли",
           "Бульдог",
           mick)        # передача хозяина
print(stan.owner.name)  # выводим имя хозяина из экземпляра класса Dog

print("=====", "\n")

# ПРАКТИКУМ к главе 13
#1
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square:
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

rec1 = Rectangle(10, 20)
sq1 = Square(15)

print(rec1.calculate_perimeter())
print(sq1.calculate_perimeter())

print("=====", "\n")

#2
class Square:
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, size):
        self.size = size
        self.s1 += size

sq1 = Square(10)
print(sq1.calculate_perimeter())
sq1.change_size(5)
print(sq1.calculate_perimeter())
sq1.change_size(-5)
print(sq1.calculate_perimeter())

print("=====", "\n")

#3
class Shape:
    def what_am_i(self):
        print("Я - фигура.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

rec1 = Rectangle(15, 20)
sq1 = Square(15)
rec1.what_am_i()
sq1.what_am_i()

print("=====", "\n")

#4
class Horse:
    def __init__(self, name, color, rider):
        self.name = name
        self.color = color
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name

fil = Rider("Филя")
horse = Horse("Стремительный", "гнедой", fil)

print(horse.rider.name)

print("=====", "\n")

# глава 14 ЕЩЕ ОБ ООП**********
# В Python классы являются объектами.

class Square:
    pass

print(Square)

print("=====", "\n")

# Переменные класса и переменные экземпляра**********
"""
У классов есть два типа переменных — переменные класса 
и переменные экземпляра класса: self.имя_переменной = значение переменной. 
Переменные экземпляра класса принадлежат объектам
Переменные класса - принадлежат объектам класса и 
позволяют обмениваться данными
между всеми экземплярами класса без использования 
глобальных переменных
"""
class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("""{} на {}""".
              format(self.width,
                   self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)
print(r1.recs[1])   # В r1 имею доступ к переменным r2

""" В r1 имею доступ к любой переменной r2 
(первое значение tuple - в этом случае)
"""
print(r1.recs[1][0])

print("=====", "\n")

# МАГИЧЕСКИЕ МЕТОДЫ**********
#p129
class Lion:
    def __init__(self, name):
        self.name = name

lion = Lion("Дилберт")
print(lion) # При этом выводе используется магический метод __repr__

# Можно переопределить, унаследованный от Object, магический метод __repr__
class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
lion = Lion("Дилберт")
print(lion) # При этом выводе используется переопределенный магический метод
# __repr__

"""
Операнды в выражении должны иметь магический метод, 
который оператор может использовать для оценки выражения. 
Например, в выражении 2 + 2 каждый объект целого числа 
имеет магический метод_ .add, вызываемый Python при 
оценке выражения. Если вы определите метод add в классе, 
то сможете использовать создаваемые им объекты как 
операнды в выражении с оператором сложения.
"""
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
print(x)    # Отдельно значение не выводят
y = AlwaysPositive(10)
# А сумму двух объектов вывести можно
print(x + y)    # Результат всегда будет положительным, потому что в
# переопределении использовано по модулю abs

print("=====", "\n")

# Ключевое слово is**********
"""
Ключевое слово is возвращает значение True, 
если два объекта являются одним и тем же объектом, 
и False в противном случае.
"""
class Person:
    def __init__(self):
        self.name = "Боб"

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

"""
Используйте ключевое слово is , чтобы проверить, 
присвоено ли переменной значение None.
"""
x = 10
if x is None:
    print("x равно None")
else:
    print("x не равно None")

x = None
if x is None:
    print("x равно None")
else:
    print("x не равно None")

print("=====", "\n")

# ПРАКТИКУМ к гл.14
#1
class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

s1 = Square(7)
s2 = Square(9)
s3 = Square(11)
print(Square.square_list)
print(s3.square_list)

#2
class Square:
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def __repr__(self):
        return ("{} на {} на {} на {}".format(self.s1,
                                            self.s1,
                                            self.s1,
                                            self.s1))
print(Square(29))

#3
def equal(o1, o2):
    print(o1 is o2)

s1 = Square(7)
s2 = Square(7)
equal(s1, s2)
s2 = s1
equal(s1, s2)

print("=====", "\n")

# Глава 15. ПРАКТИКУМ. Часть II*****



print("=====", "\n")
print("=====", "\n")
