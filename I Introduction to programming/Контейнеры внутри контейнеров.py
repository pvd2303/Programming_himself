# КОНТЕЙНЕРЫ внутри контейнеров
lists = []
rap = ["Баста",
       "Кравц",
       "Злой дух",
       "25-17"]

rock = ["Наутилус помпилиус",
        "Кино",
        "Ария"]

djs = ["Paul Oakenfold",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
#=========
rap = lists[0]
print(rap)

rap.append("Наше дело")
print(rap)
print(lists)
#==========
locations = []
tula = (54.1960, 37.6182)
moscow = (55.7522, 37.6155)

locations.append(tula)
locations.append(moscow)

print(locations)
#===========
eights = ["Эдгар Алан По",
          "Чарьз Диккенс"]
nines = ["Хемингуэй",
         "Фиджералбд",
         "Оруэл"]
autors = (eights, nines)
print(autors)
#===========
bday = {"Хемингуэй": "21.07.1899",
        "Фицджеральд": "24.09.1896"}
my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)
#============
# Список, кортеж или словарь могут быть значениями в словаре
ru = {"Расположение":
          (55.7522,
           37.6155),    # кортеж - никогда не изменяется
      "Знаменитости":
      ["Андрей Звягинцев",
       "Юрий Быков",
       "Петр Буслов"],  # список
      "факты":
          {"город":
           "Москва",
           "страна":
           "Россия"}}   # словарь
print(ru)

