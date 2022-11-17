# -*- coding: utf-8 -*-
# Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных аргументов,
# в качестве результата функция должна возвращать только позиционные аргументы с нечетными индексами и ключевые,
# значения которых являются строками


def func_1(*args, **kwargs):
    return args[1::2], [v for k, v in kwargs.items() if isinstance(v, str)]


print(func_1(1, 21, 22, 23, 25, 2, 4, 5, 6, 7, 8, a='hi', b=11, c='world', d=13))