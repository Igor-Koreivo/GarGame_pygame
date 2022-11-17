# -*- coding: utf-8 -*-
# Напишите пример любого класса и создайте его объект.
# Допишите несколько атрибутов в класс с прошлого задания, продемонстрируйте их работу.
# Допишите по 2 динамических и статических свойства в класс с предыдущего задания. Продемонстрируйте их работу.
class Primer:
    def agr(self):
        print('Hello OverOne')
    def agr1(self):
        print('Hello World')
    def agr2(self):
        print('Hello Kiki')
    default_color = 'red'
    default_weight = 10
    def __init__(self, model, color):
        self.model = model
        self.color = color
object = Primer('square','blu')

print(dir(Primer))
print(object.default_weight)
print(object.model, object.color)
# pr = Primer()
# pr.agr()
# pr.agr1()
# pr.agr2()