# -*- coding: utf-8 -*-
# Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке. Список должен быть
# сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
import random


def rec_sum(lst):
    if not len(lst):
        return 0
    return lst[0] + rec_sum(lst[1:])


lst = [random.randint(1, 101) for i in range(10)]
print('Случайный список: ', lst)
print('Сумма чиселл в списке: ', rec_sum(lst))