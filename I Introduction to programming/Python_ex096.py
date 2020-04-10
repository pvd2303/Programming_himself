def even_odd():
    while True:
        n = input("Введите число:")
        if n == "exit":
            exit()
        else:
            n = int(n)
            if n % 2 == 0:
                print("n - четное")
            else:
                print("n - нечетное")

even_odd()