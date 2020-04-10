# СПИСКИр
fruit = ["Яблоко", "Апельсин", "Персик"]
print(fruit)
fruit.append("Банан")
fruit.append("Дыня")
print(fruit)

random = []
random.append(True)
random.append(100)
random.append(1.1)
random.append("Привет")
print(random)

print(fruit[2])

for fr in fruit:
    print(fr)

colors = ["синий", "зеленый", "желтый"]
print(colors)
colors[2] = "красный"
print(colors)

colors = ["синий", "зеленый", "желтый"]
item = colors.pop()
print(colors)
print(item)
print(colors)

# Сложение списков
colors1 = ["синий" , "зеленый", "желтый"]
colors2 = ["оранжевый", "розовый", "черный"]
print(colors1 + colors2)

# Проверка наличие элемента в списке
colors = ["синий", "зеленый", "желтый"]
print("зеленый" in colors)

# Проверка отсутствия элемента в списке
print("черный" not in colors)

# Получить длину списка
print(len(colors))

# Пример использования списка на практике
colors = ["фиолетовый",
          "оранжевый",
          "зеленый"]
guess = input("Угадайте цвет: ")

if guess in colors:
    print("Вы угадали!")
else:
    print("Неправильно! Попробуйте еще.")

