# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


print('Задача № 18')
print()
import random

GetUserNum = int(input("Введите количество числе в массиве: "))
array = [0] * GetUserNum
for i in range(GetUserNum):
    array[i] = random.randint(1,10)
digit = int(input("Введите искомое близкое число: "))
min_dif = array[0]
for i in array:
    if abs(digit - i) < abs(min_dif-digit):
        min_dif = i
        
print(f"Самое близкое число к {digit} в массиве {array} является {min_dif}")