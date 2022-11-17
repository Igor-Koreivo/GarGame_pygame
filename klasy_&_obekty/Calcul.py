# -*- coding: utf-8 -*-
class Calc:
    def __init__(self):
        self.vvod()

    def plus(self,a):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def dele(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b

    def umn(self):
        return self.a * self.b

    def vvod(self):
        self.a = int(input("Введите первое число: "))
        self.b = int(input("Введите второе число: "))


while True:
    ex = Calc()
    c = input("Введите операцию(+,*,/,-): ")
    if c == '+':
        print(ex.plus())
    elif c == "-":
        print(ex.minus())
    elif c == '*':
        print(ex.umn())

    elif c == '0':
        break
    else:
        print(ex.dele())