# Найдите сумму цифр трехзначного числа
def task2():
    n = int(input("Введите число: "))
    i = n // 100
    j = n // 10 % 10
    k = n % 10
    print(f"{i} + {j} + {k} = {i + j + k}")

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
def task4():
    n = int(input("Введите число: "))
    print(f"Петя - {int(n / 6)}, Сережа - {int(n / 6)}, Катя - {int(4 * n / 6)}")

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3 + 8 + 5 = 9 + 1 + 6. Вам требуется написать программу, которая проверяет счастливость билета
def task6():
    n = input("Введите число: ")
    part1 = int(n[0]) + int(n[1]) + int(n[2])
    part2 = int(n[3]) + int(n[4]) + int(n[5])
    print("yes" if part1 == part2 else "no")

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника)
def task8():
    n = int(input("Введите число n: "))
    m = int(input("Введите число m: "))
    k = int(input("Введите число k: "))
    print("yes" if k % n == 0 or k % m == 0 else "no")