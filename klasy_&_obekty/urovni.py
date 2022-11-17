# -*- coding: utf-8 -*-
# Продемонстрируйте разные уровни доступа на примере любого класса.
class Urovni:
    a = 'Public class'
    _b = 'Protected class'
    __c = 'Private class'


obj = Urovni()
print(obj.a)
print(obj._b)
print(obj._Urovni__c)
