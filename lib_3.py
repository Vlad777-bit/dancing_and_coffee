def hanoi(n, first, third, second):
    if n == 1:
        print("Переместить диск 1 с", first, "на", third)
        return
    hanoi(n-1, first, second, third)
    print("Переместить диск", n, "с", first, "на", third)
    hanoi(n-1, second, third, first)

n = int(input("Введите количество дисков: "))
hanoi(n, 'A', 'C', 'B')
