
#Напишите программу, которая на вход принимает 
#5 чисел и находит максимальное из них.
# Вариант 1
# a = input().split()
# print(a)
# max = int(a[0])
# for i in range(len(a)):
#     if int(a[i])>max:
#         max = int(a[i])
# print(max)
# Вариант 2
# a = map(int, input().split())
# a = list(a)
# print(max(a))


#Напишите программу, которая будет на вход принимать число
# N и выводить числа от -N до N
# n = int(input('Введите число: '))
# a = []
# b = ''
# for i in range(-n,n+1):
#     a.append(i) #добавляет элемент в конец списка
#     print(f' {i} ', end='')
#     b += f' {i}'
# print()
# print(a)
# print(b)


#Напишите программу, которая будет принимать на вход дробь и 
# показывать первую цифру дробной части числа.
# a = float(input('Введите число: '))
# a = int(a*10)%10
# print(a)


#Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно ((5 и 10) или 15), но не 30.
# 45 -> yes
# 20 -> yes
# 60 -> no
# 75 -> yes
a = int(input('Введите число: '))
if (a%5 == 0 or a%10 == 0) and a%30!= 0:
    print('yes')
elif a%15 == 0 and a%30 != 0:
    print('yes')
else:
    print('no')