# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
def task16():
    import random
    n = int(input("Введите количество элементов списка: "))
    lst = [random.randint(0, n) for i in range(0, n)]
    print(f"Сгенерированный список: {lst}")
    x = int(input("Введите элемент для подсчета: "))
    print(f"Кол-во элементов в списке: {lst.count(x)}")

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
def task18():
    import random
    n = int(input("Введите количество элементов списка: "))
    lst = [random.randint(0, n) for i in range(0, n)]
    print(f"Сгенерированный список: {lst}")
    x = int(input("Введите элемент для нахождения максимально близкого к нему значения: "))
    dct = {}
    for i in range(len(lst)):
        if abs(x - lst[i]) not in dct:
            dct[abs(x - lst[i])] = lst[i]

    print(f"Максимально близкое значение к элементу {x}: {dct[min(dct)]}")

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка;
# K – 5 очков; 
# J, X – 8 очков;
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы
def task20_1():
    dct = dict(
        aeioulnstrавеинорст = 1,
        dgдклмпу = 2,
        bcmpбгёья = 3,
        fhvwyйы = 4,
        kжзхцч = 5,
        jxшэю = 8,
        qzфщъ = 10
    )
    word = input("Введите слово: ").lower().strip()
    total = 0
    for ch in word:
        for key in dct:
            for letter in key:
                if letter == ch:
                    total += dct[key]
    print(f"Очки: {total}")

def task20_2():
    from re import findall
    word = input("Введите слово: ").lower().strip()
    dct = dict(
        aeioulnstrавеинорст = 1,
        dgдклмпу = 2,
        bcmpбгёья = 3,
        fhvwyйы = 4,
        kжзхцч = 5,
        jxшэю = 8,
        qzфщъ = 10
    )
    total = 0
    for regex in dct:
        pattern = r"[{}]".format(regex)
        finded = findall(pattern, word)
        if len(finded) > 0: total += len(finded) * dct[regex]

    print(f"Очки: {total}")