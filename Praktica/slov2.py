# 1.Выведите общее время звучания всех песен.
# 2.Создайте список песен, время звучаниях которых больше 5 минут.
# 3.Создайте новый словарь тех песен, в название которых состоит из одного слова.
violator_songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68 }
print('Общее время всех песен -', sum(violator_songsdict.values()))
print('Список песн больше пяти минут: ')
for k, v in violator_songsdict.items():
    if v > 5:
        print(f'Песня - {k}, Время - {v}')

a = {d : violator_songsdict[d] for d in violator_songsdict.keys() if not ' ' in d}
print("Словарь песен у которых название состоит из одного слова -", a)