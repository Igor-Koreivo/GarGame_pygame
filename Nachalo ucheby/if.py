a = 7
if a > 0:
    b = a + 4
    if b == 3:
        print('3')
    elif b > 0:
        print(b)
    else:
        print('Hello')
elif a == 0:
    print('0')
elif a < 0:
    print('a<0')
else:
    print('else')

a = bool({})
b = bool([1, 2, 3])
dictionary = {5: a, b: 6, True: 7, 8: 1}

if dictionary[8]:
    print(a)
