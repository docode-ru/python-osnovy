# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения и
# исправьте все ошибки


# создание пустого списка
empty_list = []

# определите тип
assert __ == type(empty_list)

# доступ к элементам списка
noms = ['peanut', 'butter', 'and', 'jelly']
assert __ == noms[0]
assert __ == noms[3]
assert __ == noms[1]

# какие элементы списка вернуться
# в результате применения опратора среза
assert __ == noms[0:1]
assert __ == noms[0:2]
assert __ == noms[2:]
assert __ == noms[:2]
assert __ == noms[-1]
assert __ == noms[-2:]

assert __ == noms[2:]*3
assert __ == noms[-2:]+noms[:2]

assert __ == 'peanut' in noms
assert __ == 'umbrella' not in noms