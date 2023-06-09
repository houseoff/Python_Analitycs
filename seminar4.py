# Напишите программу, которая принимает на вход строку
# и отслеживает, сколько раз каждый символ уже встречался
# Количество повторов добавляется к символам с помощью постфикса формата _n.

def task25_1():
    string = "a a a b c a a d c d d"
    dct = {}
    result_str = ""
    for ch in string.split():
        if ch in dct: dct[ch] += 1
        else:         dct[ch] = 1

        if dct[ch] == 1: result_str += "{} ".format(ch)
        else:            result_str += "{}_{} ".format(ch, dct[ch] - 1)
    print(result_str)

def task25_2():
    string = "a a a b c a a d c d d"
    lst = string.split()
    result_str = ""

    for i in range(len(lst)):
        count = lst[0:i].count(lst[i])

        if count > 0: result_str += "{}_{} ".format(lst[i], count)
        else: result_str += "{} ".format(lst[i])
    
    print(result_str)

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов
# Определите, сколько различных слов содержится в этом тексте
def task27():
    string = """She sells sea shells on the sea shore 
        The shells that she sells are sea shells I'm sure. 
        So if she sells seashells on the sea shore 
        I'm sure that the shells are sea shore shells"""
    st = set(string.lower().replace('.','').split())
    print(len(st))

# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# "Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)"
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам
def task29():
    maxx = 0
    while (n:=int(input("Введите число: "))) != 0:
        if n > maxx: maxx = n
    print(f"Максимум: {maxx}")

task29()
    


