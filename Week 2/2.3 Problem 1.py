#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. 
# Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

# Напишите программу, на вход которой даются четыре числа a a a, b b b, c c c и d d d, каждое в своей строке. 
# Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] [a; b] [a;b] на все числа 
# отрезка [c;d] [c;d] [c;d].

# Числа a, b, c и d являются натуральными и не превосходят 10, a≤b a \le b a≤b, c≤d c \le d c≤d.

# Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции.
# Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец 
# и строка таблицы.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for x in range(c,d+1):
    print('\t', x, end='')
for y in range(a,b+1):
    print('\n', y, end='')
    for x in range(c,d+1):
        print('\t', x*y, end='')
