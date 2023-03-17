# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

GetUserNumber = int(input('Введите трехзначное число: '))
Summ = 0
index = 0
while index < 3:
    Summ += (GetUserNumber % 10)
    GetUserNumber = GetUserNumber // 10
    index += 1
print(f'Сумма цифр равна {Summ}')