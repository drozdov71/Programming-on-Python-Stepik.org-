#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.
a = float(input())
b = float(input())
c = str(input())
if b == 0 and (c == '/' or c == 'mod' or c == 'div'):
    print("Деление на 0!")
elif c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
elif c == 'mod':
    print(a%b)
elif c == 'div':
    print(a//b)
elif c == 'pow':
    print(a**b)
