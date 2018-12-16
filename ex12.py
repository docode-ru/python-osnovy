# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения и
# исправьте все ошибки

empty_dict = {}
assert dict == type(empty_dict)

color_codes = {'red': 'F00', 'green': '0F0', 'blue': '00F', 'black': 'FFF'}

assert __ == color_codes['green']
assert __ == color_codes['blue']
assert __ == color_codes['red']
assert __ == color_codes.keys()
assert __ == color_codes.values()

color_codes['white'] = __
assert color_codes['white'] == '000'

# лучше избегать добавления данных других типов
color_codes[1] = 'wrong item'
assert __ == color_codes[1]