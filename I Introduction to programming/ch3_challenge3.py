x = 26


if x <= 10:
    print("x меньше или равно 10")
elif 10 < x <= 25:
    print("x больше 10 и меньше или равно 25")
elif x > 25:
    print("x больше 25")

# Это решение изящнее
if x <= 10:
    print("x меньше или равно 10")
elif x <= 25:
    print("x больше 10 и меньше или равно 25")
else:
    print("x больше 25")