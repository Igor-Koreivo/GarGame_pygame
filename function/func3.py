# -*- coding: utf-8 -*-
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если
# оно простое, и False - иначе.
x = int(input('Введите число от 0 до 1000: '))


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False

    return True


print(f'Число {x} простое (True) или нет (False) :', is_prime(x))