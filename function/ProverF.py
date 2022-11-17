# -*- coding: utf-8 -*-
# Если в функцию передаётся кортеж, то посчитать длину всех его слов.  Если список, то посчитать кол-во букв и чисел
# в нём. Число – кол-во нечётных цифр. Строка – количество букв. Сделать проверку со всеми этими случаями.
def func(a):
    if type(a) == tuple:
        print('Длина слов кортежа:', len(a))
    elif type(a) == list:
        print('Количество букв в списке: ', len(list(filter(lambda x: type(x) == str, a))),
              '. Количество чисел в списке: ', len(list(filter(lambda x: type(x) in (int, float), a))))
    elif type(a) == int:
        print('Количество нечётных цифр в числе: ', sum(int(i) % 2 for i in str(a)))
    elif type(a) == str:
        print('Количество букв в строке', len(a))

func(('hi', 'world', 'tt', '12', '14'))
func([1, 2, 33, 'a', 'b', 'c', 'h', 'w', 7])
func(12345678901111)
func('afadfdsfhhwesgdh')