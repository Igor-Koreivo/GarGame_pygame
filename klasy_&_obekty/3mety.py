# -*- coding: utf-8 -*-
# Файл с кодом, демонстрирующий работу разных видов методов класса.
class Myclas():
    def agr(self):
        print('Hello Usual Method')

    @staticmethod
    def staticmet():
        print('Hello Static Method')

    @classmethod
    def classmet(cls):
        print('Hello Class Method')


my_obj = Myclas()
my_obj.agr()
my_obj.staticmet()
my_obj.classmet()