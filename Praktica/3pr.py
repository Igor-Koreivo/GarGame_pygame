# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в веденном с клавиатуры слове.
# (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а также сколько всего букв в слове, сколько гласных и согласных.
a = 'aaaaAAAAccccCCCxx'
t_upper = 0
t_lower = 0
glas = 'aeuioy'
for i in range(len(a)): # т.к. индекс с 0, а len
    if a[i].isupper():
        t_upper += 1
    elif a[i].islower():
        t_lower += 1
glasn = 0
soglasn = 0
for k in a:
    if k.lower() in glas:
        glasn += 1
    else:
        soglasn += 1
print('Всего букв в слове:',len(a),'.  Пар верхнего регистра:',t_upper//2,
      '.  Пар нижнего регистра:',t_lower//2,'.  Кол-во гласных букв:',glasn,'.  Кол-во соглсных букв:',soglasn)
