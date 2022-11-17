# -*- coding: utf-8 -*-
# Примеры видов полиморфизма.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Я кот по имени {self.name}. Мне {self.age} лет (года).")

    def make_sound(self):
        print("Мяу")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Я собака по имени {self.name}. Мне {self.age} лет (года).")

    def make_sound(self):
        print("Гаф гаф")


cat1 = Cat("Мурзик", 4)
dog1 = Dog("Барс", 5)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
