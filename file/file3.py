# В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить
# количество в ней символов.
f = open('3.txt', 'r')
print(f.readlines())

print('Количество строк:', sum(1 for i in open('3.txt', 'r')))  # кол-во строк

f = open('3.txt', 'r')
print('Количество символов по строчно:')
for line in f.readlines():
    print(len(line), end=' | ')
f.close()
print("в файле '3.txt'")