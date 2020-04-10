# МОДУЛИ
import math
print(math.pow(2, 3))

import random
print(random.randint(1, 100))

import statistics
# среднее
nums = [1, 5, 33, 12, 46, 33, 2]
print(statistics.mean(nums))

# медиана
print(statistics.median(nums))

# мода
print(statistics.mode(nums))

import keyword
print(keyword.iskeyword("for"))
print(keyword.iskeyword("football"))

# можно распечатать состав функций и тд любого встроеного модуля
# print(help("math"))
# print(dir(math))

#1
#print(help("statistics.median"))
print(statistics.median([1, 3, 5, 7]))
print(statistics.median([1, 3, 5]))

#2
import cubed
print(cubed.cube(5))