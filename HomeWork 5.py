# # 1. У вас есть массив чисел. Напишите три функции, которые вычисляют
# # сумму этих чисел: с for-циклом, с while-циклом, с *рекурсией.
#
# a = {1,2,3,4,5,6,7,100,12}
#
# def for_func(set):
#     s = 0
#     for i in set:
#         s += i
#     return print(s)
#
# for_func(a)
#
#
# def while_func(set):
#     s = 0
#     while set:
#         s += set.pop()
#
#     return print(s)
#
# while_func(a)
#
#
# a = {1,2,3,4,5,6,7,100,12}
# s = 0
#
# def rec_func(set):
#     if len(set) == 0:
#         return 0
#     s = set.pop() + rec_func(set)
#     return s
#
# print (rec_func(a))
#
# # 2. Напишите функцию, которая создаёт комбинацию двух списков таким
# # образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
#
# a = [1, 2, 3]
# b = [11, 22, 33]
#
# def splt(a,b):
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     return c
#
# print (splt(a,b))
#
# # 3. Существует ли треугольник с заданными сторонами.
#
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a + b >= c and b + c >= a :
#     print ('Ok')
# else: print ('Not OK')
#
# # 6. Заданы M строк символов, которые вводятся с клавиатуры. Каждая строка
# # представляет собой последовательность символов, включающих в себя
# # вопросительные знаки. Заменить в каждой строке все имеющиеся
# # вопросительные знаки звёздочками.
#
# print('Input q-ty of str: ')
# m = int(input())
# s = []
# for i in range(m):
#     print('Input ' + str(i+1) + 'st line')
#     s.append(input())
#     s[i] = s[i].replace('?', '*')
#
# print(s)
#
# 7. Системная дата имеет вид 2009-06-15. Нужно преобразовать это значение
# в строку, строку разделить на компоненты (символ→разделитель→дефис),
# # потом из этих компонентов сконструировать нужную строку. (2009-06-15 ->
# # 15/06/2009)
#
# a = '2009-06-15'
# a = a.split('-')
# a.reverse()
# a = '/'.join(a)
#
# print(a)

# # 8. Задан вес в граммах. Определить вес в тоннах и килограммах.
#
# a = int(input())
# print(a / 1000, 'kg')
# print(a / 1000000, 'tons')

# 9. Имеется коробка со сторонами: A × B × C. Определить, пройдёт ли она в
# дверь с размерами M × K.
#
#
# print('Input box size AxBxC')
# a = int(input('Side A: '))
# b = int(input('Side B: '))
# c = int(input('Side C: '))
# print('Input door size MxK')
# m = int(input('DoorSide M: '))
# k = int(input('DoorSide K: '))
#
# s_ab = a * b
# s_ac = a * c
# s_bc = b * c
# s_door = m * k
#
# if s_ab <= s_door or s_ac <= s_door or s_bc <=s_door:
#     print('OK')
# else: print('not OK')

# 10. Можно ли из бревна, имеющего диаметр поперечного сечения D,
# # выпилить квадратный брус шириной A?
#
#
# d = int(input('Diametr D: '))
# a = int(input('Side A: '))
#
# if d ** 2 >= 2 * (a ** 2):
#     print('OK')
# else: print('not OK')
#
# 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# верхнее или нижнее, в купе или боковое.
#
# num = int(input('Input seat number '))
#
# if num <= 36 and num % 2 == 0:
#     seat_side = 'Coupe'
#     seat_lvl = 'Top'
# elif num <= 36 and num % 2 != 0:
#     seat_side = 'Coupe'
#     seat_lvl = 'Bottom'
# elif num > 36 and num % 2 != 0:
#         seat_side = 'Side'
#         seat_lvl = 'Bottom'
# else:
#     seat_side = 'Side'
#     seat_lvl = 'Bottom'
#
# print('You place is ', seat_lvl, ' and ', seat_side)

# 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# монетой 2 грн., если это возможно.
#
# s_money = int(input('Input your sum of money: '))
# pocket = []
#
# for i in [500, 100, 10, 2]:
#     while (s_money - i) >= 0 and s_money != 1:
#         pocket.append(i)
#         s_money -= i
#
# if not s_money:
#     s_500 = pocket.count(500)
#     print('Banknote (500) - ', s_500)
#     s_100 = pocket.count(100)
#     print('Banknote (100) - ', s_100)
#     s_10 = pocket.count(10)
#     print('Banknote (10) - ', s_10)
#     s_2 = pocket.count(2)
#     print('Banknote (2) - ', s_2)
# else:
#     print ('Sorry, you cant change this sum')

# 13. Пользователь вводит число n, программа должна проверить является ли
# оно простым и сообщить об этом.
#
# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")

# 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# Числа M, a и b вводит пользователь.
#
# M = int(input('Input M: '))
# a = int(input('Input a: '))
# b = int(input('Input b: '))
#
# print ('Multiply table: ')
#
# for a in range (a-1, b):
#     a += 1
#     print (M, "x", a, "=", M * a)
#
# 15. Дан одномерный массив числовых значений, насчитывающий N
# элементов. Поменять местами элементы, стоящие на чётных и нечётных
# местах: A[1] ↔ A[2]; A[3] ↔ A[4] …
#
# a = [1,2,3,4,5,6,7,8]
#
# print(a)
#
# for i in range(0, len(a), 2):
#     a[i], a[i+1] = a[i+1], a[i]
#
# print(a)

# 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.

# lower = int(input('Input lower number in range: '))
# upper = int(input('Input upper number in range: '))
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)