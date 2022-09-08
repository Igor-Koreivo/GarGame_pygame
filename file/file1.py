# Ввести в файл ‘input.txt’ 2 числа в одну строку через пробел. Вывести в файл ‘output.txt’ их разность.
a = int(input('Введите первре число:', ))
b = int(input('Введите второе число:', ))
with open('input.txt', 'w') as f:
    f.write(f'{a} {b}')
with open('output.txt', 'w') as f_out:
    f_out.write(f'{a-b}')
f = open('input.txt', 'r')
print('Текст из input.txt:', f.readline())
f.close()
f_out = open('output.txt', 'r')
print('Текст из output.txt:', f_out.readline())
f_out.close()