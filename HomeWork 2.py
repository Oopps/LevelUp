# 1. Напишите программу, которая просит пользователя что-нибудь ввести с клавиатуры. Если он вводит какие-нибудь данные, то на экране должно выводиться сообщение "ОК".
# Если он не вводит данные, а просто нажимает Enter, то программа ничего не выводит на экран.

a = input()
if a != (''):
    print('OK')

# 2. Напишите программу, которая запрашивает у пользователя число. Если оно больше нуля, то в ответ на экран выводится число 1. Если введенное число не является положительным, то на экран  должно выводиться -1.

a = int(input())
if a > 0:
    print(1)
else: print(-1)

# 3. Напишите программу которая просит пользователя ввести число и проверяет есть ли это число в массиве. Массив взять произвольный.

a = {1,2,3,4,5,6,7,100,12}
b = int(input())
if b in a:
    print('OK')

# 4. Такая же как и 3, но проверяем есть ли такой ключ в словаре. Словарь так же произвольный.

a = {1,2,3,4,5,6,7,100,12}
b = int(input())
for i in range(len(a)):
    if b == i:
        print('OK')
