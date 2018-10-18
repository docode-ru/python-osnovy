# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения и
# исправьте все ошибки

colors = ( 'Red' , 'Green' , 'Red' , 'Blue' , 'Red' )

newcolors = colors[:3]

assert __ == colors[0]
assert __ == colors[-1]

assert __ == colors[1:3]
assert __ == colors[2:]
assert __ == colors[-1:]
assert __ == colors[:-1]
assert __ == colors[-4:-2]
assert __ == colors[:2]*2

assert __ == newcolors + ('Yellow', 'Gold')