# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

print('Задача № 10')

from random import randint

GetUserNumber = int(input("Введите число монеток: "))
numbers = []
coin_obverse = 0
coin_reverse = 0

for i in range(GetUserNumber):
    numbers.append(randint(0, 1))

print(numbers)

for i in range(len(numbers)):
    if numbers[i] == 1:
        coin_obverse += 1
    elif numbers[i] == 0:
        coin_reverse += 1
    else:
        print("Что-то пошло не так...")

if coin_obverse > coin_reverse:
    print(coin_reverse)
else:
    print(coin_obverse)