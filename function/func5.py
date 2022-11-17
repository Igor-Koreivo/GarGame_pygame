# -*- coding: utf-8 -*-
# Напишите декоратор, который будет считать, сколько раз была вызвана декорируемая функция.
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper
@counter
def f():
    pass
f()
f()
f()
f()
f()
print('Cколько раз была вызвана декорируемая функция - ', f.count, 'раз.')