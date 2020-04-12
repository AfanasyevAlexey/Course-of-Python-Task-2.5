# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# for i in range(1,6):
#     print(str(i) + '. ' + '0')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

# m = 10
# n = 5
# count = 0
# print('Введите любые 10 чисел')
# for i in range(1, m + 1):
#     m = int(input("Введите число " + str(i) + ": "))
#     while m > 0:
#         if m % 10 == n:
#             count += 1
#         m = m // 10
# print()
# if any([(count == 1), (count == 21), (count == 31), (count == 41), (count == 51)]):
#     print('В данном цикле присутствует', count, 'цифра со значением "5"')
# elif any([(count == 2), (count == 22), (count == 32), (count == 42), (count == 52),
#           (count == 3), (count == 23), (count == 33), (count == 43), (count == 53),
#           (count == 4), (count == 24), (count == 34), (count == 44), (count == 54)]):
#     print('В данном цикле присутствует', count, 'цифры со значением "5"')
# else:
#     print('В данном цикле присутствует', count, 'цифр со значением "5"')


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
Добавил небольшую вариацию ответов для вводимых значений.
'''

# sum_of_numbers = 0
#
# for i in range(1, 101):
#     sum_of_numbers += i
# print(sum_of_numbers)
# if sum_of_numbers < 0: print('negative meaning')
# elif sum_of_numbers > 0: print('positive value')
# else:
#     print('zero')

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

# multiplication = 1
# for i in range(1, 11):
#     multiplication *= i
# print('\nПроизведение ряда чисел от 1 до 10 =', multiplication)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 5690
#
# while integer_number > 0:
#     print(integer_number % 10)
#     integer_number = integer_number // 10

'''
Задача 6
Найти сумму цифр числа.
'''

# i = 2598
# print('\nСумма цифр введенного числа =', sum(int(c) for c in str(i)))

'''
Задача 7
Найти произведение цифр числа.
'''

# i = 2859
# number_production = 1
# while i > 0:
#     number_production *= i % 10
#     i = i // 10
# print('\nПроизведение цифр введенного числа =', number_production)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

# integer_number = int(input('\nВведите любое число '))
# print('\nЕсть ли в веденном числе цифра "5"?')
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('\nДа')
#         break
#     integer_number = integer_number//10
# else: print('\nНет')

'''
Задача 9
Найти максимальную цифру в числе
'''

# i = 3598
# max = i % 10
# i = i // 10
# while i > 0:
#     if i % 10 > max:
#         max = i % 10
#     i = i // 10
# print('\nМаксимальная цифра в веденном числе: ', max)

'''
Задача 10
Найти количество цифр 5 в числе
'''

# num = int(input('\nВедите любое число '))
# a = 5
# count = 0
# while num > 0:
#     if num % 10 == a:
#         count += 1
#     num = num // 10
# print('\nВ данном числе присутствует', count, 'цифр со значением "5"')