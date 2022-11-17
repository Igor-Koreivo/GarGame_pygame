# -*- coding: utf-8 -*-
# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно длине слова, выводить
# все гласные, иначе согласные; если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.
class method:
    def func(self, agr):
        if isinstance(agr, str):
            if sum(x in "ауоыиэюяеё" for x in agr.lower()) * sum\
                        (x in "бвгджзйклмнпрстфхцчшщ" for x in agr.lower()) <= len(agr):
                return ''.join([x for x in agr if x.lower() in "ауоыиэюяеё"])
            else:
                return ''.join([x for x in agr if x.lower() in "бвгджзйклмнпрстфхцчшщ"])
        elif isinstance(agr, int):
            return sum(int(x) for x in str(agr) if x in "2468") * len(str(agr))
    def fuc_2(self, agr):
        return len(str(agr))
obj = method()
test_1 = obj.func("Как дела? Нормально тут все работает?")
test_2 = obj.func("Ааааааа крокодилы, бегемоты, аааааа обезьяны, кашалоты !")
test_3 = obj.func(123225)

print(test_1)
print(test_2)
print(test_3)