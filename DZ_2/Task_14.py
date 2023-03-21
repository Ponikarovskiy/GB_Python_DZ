# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

print('Задача № 14')
print()
number = int(input("Введите натуральное число: "))
index = 0
result = 1
while result < number:
    result = 2 ** index
    if result < number:
        print(result, end = " ")
    index += 1