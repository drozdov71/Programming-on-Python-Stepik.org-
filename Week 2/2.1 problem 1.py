#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и 
# после первого введенного нуля выводит сумму полученных на вход чисел
a = int(input()) # read number
s = 0 # that will be sum soon
while a != 0: # write number until one of them will be 0
    s = s + a # summing numbers that are not = 0
    a = int(input()) # Continue read numbers
print(s)

