# -*- coding: utf-8 -*-
import string


class Alphabet:  # алфавит
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)  # вывод всех букв

    def letters_num(self):
        len(self.letters)  # для вывода кол-во букв


class EngAlphabet(Alphabet):  # анг. алфавит
    def __init__(self):
        super().__init__('En', string.ascii_letters)

    __letters_num = 26

    def is_en_letter(self, letters):  # провека текска на англ. буквы
        if letters.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num  # вывод кол-во букв

    @staticmethod
    def example():
        print("Don’t Worry, Be Happy")


# Тесты
if __name__ == '__main__':
    eng_alfabet = EngAlphabet()
    eng_alfabet.print()
    print(eng_alfabet.letters_num())
    print(eng_alfabet.is_en_letter('F'))
    print(eng_alfabet.is_en_letter('Щ'))
    EngAlphabet.example()
