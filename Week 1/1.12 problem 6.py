#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали 
# для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и 
# произносит его вслух: "n программистов".
# Для того, чтобы это звучало правильно, для каждого n n n нужно использовать верное окончание слова.
# Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число 
# в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог 
# нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
#  В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, 
# как минимум до 1000 человек.
n = int(input())
if n%10 ==1 and n%100 !=11:
    print(n, 'программист')
elif (n%10 == 2 and n%100 !=12) or (n%10 == 3 and n%100 !=13) or (n%10 == 4 and n%100 !=14):
    print(n, 'программиста')
else:
    print(n, 'программистов')

