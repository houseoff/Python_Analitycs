# Заполните массив элементами арифметической прогрессии
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n - 1) * d
# Каждое число вводится с новой строки
def input_number():
    while True:
        try:
            n = int(input())
            break
        except:
            print("Вы ошиблись при вводе числа! Пожалуйста, повторите ввод")
    return n

def get_arithmetic_progression(a1: int, d: int, count: int):
    prog = []
    for n in range(1, count + 1):
        prog.append(a1 + (n - 1) * d)
    return prog

def task30():
    print("Введите первый элемент арифметической прогрессии:", end=' ')
    a1 = input_number()
    print("Введите разность арифметической прогрессии:", end=' ')
    d = input_number()
    print("Введите количество элементов прогрессии:", end=' ')
    count = input_number()
    print(get_arithmetic_progression(a1, d, count))

# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
def filter_by_range(lst: list, left: int, right: int):
    return list(filter(lambda x: left <= x <= right, lst))

def task32():
    from random import randint
    lst = [randint(-20, 20) for _ in range(0, 10)]
    print(f'Исходный список:', lst)
    print(f'Отфильтрованный список:', filter_by_range(lst, -8, 10))
