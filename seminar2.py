# По данному целому неотрицательному N вычислите значение N! = 1 * 2 * ... * N
# Решить задачу, используя цикл while
def task9():
    n = int(input("Введите число: "))
    i = 2
    factorial = 1
    if n > 2:
        while i <= n:
            factorial *= i
            i += 1
    print(factorial)

# Дано натуральное число a > 1. Определите, каким по счету числом Фибоначчи оно является.
# Если a не является числом Фибоначчи - выведите число -1
def task11():
    a = int(input("Введите число: "))
    fib_1 = 1
    fib_2 = 1
    position = 4
    while fib_2 < a:
        if fib_1 + fib_2 == a: break
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        position += 1
    else: position = -1
    print(position)

# Дано: количество дней N и температуры для каждого дня от -50 до 50.
# Требуется найти наибольшее кол-во дней с температурой больше 0
def task13():
    import random
    n = int(input("Введите число дней: "))
    lst = [random.randint(-50, 51) for i in range(n)]
    count = max = 0
    for el in lst:
        if el > 0: 
            count += 1
            if count > max: max = count
        else: count = 0
    print(f"Температуры: {lst}")
    print(f"Оттепель: {max} дн.")

# Найти максимум и минимум
def task15():
    import random
    n = int(input("Введите количество арбузов: "))
    lst = [random.randint(1, 16) for i in range(n)]
    print(f"Веса арбузов: {lst}")
    max = min = lst[0]
    for el in lst:
        if el > max: max = el
        if el < min: min = el
    print(f"Минимальный вес: {min}, максимальный вес: {max}")