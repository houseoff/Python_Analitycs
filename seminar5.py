# Найти N-ое число Фибоначчи через рекурсию
def fib(num):
    if num in [0,1]:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

def task31():
    n = int(input("Введите число: "))
    print(fib(n))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные
def replace_from_max_to_min(lst):
    maxx = max(lst)
    minn = min(lst)
    for i in range(len(lst)):
        if lst[i] == maxx: lst[i] = minn
    return lst

def task33():
    lst = [1, 3, 2, 5, 5 ,4]
    print(replace_from_max_to_min(lst))

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
def is_simple(num):
    if num < 0 or num in [0,1]: return False

    for i in range(2, num // 2 + 1):
        if num % i == 0: return False
    return True

def task35():
    n = int(input("Введите число: "))
    print(is_simple(n))

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
def print_reverse(n):
    x = int(input("Введите число: "))
    if n == 1: return f"{x}"
    return print_reverse(n - 1) + f" {x}"

def task37():
    n = int(input("Введите число: "))
    print(print_reverse(n))
