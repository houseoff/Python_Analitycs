# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии
def pow_recursion(a, b):
    if b == 0: return 1
    if b == 1: return a
    return a * pow_recursion(a, b - 1)

def task26():
    a = int(input("Введите число: "))
    b = int(input("Введите степень: "))
    print(pow_recursion(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел
# Из всех арифметических операций допускаются только +1 и -1
# Также нельзя использовать циклы.
def sum_recursion(a, b):
    if b == 0: return a
    return 1 + sum_recursion(a, b - 1)

def task28():
    a = int(input("Введите 1-ое число: "))
    b = int(input("Введите 2-ое число: "))
    print(sum_recursion(a, b))
