# Дан список чисел. Определить, сколько в нём встречается разных чисел
def task17():
    import random
    lst = [random.randint(0, 10) for i in range(8)]
    print(f"Исходный список: {lst}")
    print(f"Количество различных чисел в списке: {len(set(lst))}")

# Дана последовательность из N целых чисел и число К.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо
def task19():
    n = int(input("Введите кол-во элементов: "))
    shift = int(input("Введите число сдвигов: "))
    lst = [i for i in range(1, n + 1)]
    len_lst = len(lst)
    print(f"Исходный список: {lst}")

    if shift < 0:
        shift = -shift
        print(f"Сдвиг влево на {shift} эл.: ", end='')
        shift %= len_lst
    elif shift == 0:
        print(f"Сдвиг на {shift} эл.:  ", end='')
    else:
        shift %= len_lst
        print(f"Сдвиг вправо на {shift} эл.: ", end='')
        shift = len_lst - shift
    
    print(lst[shift:] + lst[:shift])

# Напишите программу для печати всех уникальных значений в словаре
def task21_1():
    lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    set_lst = set()
    for el in lst:
        for v in el.values():
            set_lst.add(v)

    print(set_lst)

def task21_2():
    lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    set_lst = set()
    for el in lst:
        set_lst = set_lst.union(set(el.values()))

    print(set_lst)

# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего
def task23():
    import random
    lst = [random.randint(0, 10) for i in range(10)]
    count = 0
    print(f"Исходный список: {lst}")
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            print(f"Найдена пара: {lst[i + 1]} > {lst[i]}")
            count += 1
    print(f"Общее кол-во пар: {count}")

