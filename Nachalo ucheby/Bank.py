#В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс
# на карте. Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на
# карте.
a = int(input("Введите ваш баланс карты: "))
buy = int( )
r = 0
while a - buy:
    buy = int(input('Введите сумму которую вы потратили: '))
    a = a - buy
    r = r + 1
    if a < 0:
        print('На вашем балансе не достаточно средств')
        break
    print('Остаток: ', a, 'Номер операции: ', r)