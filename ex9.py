# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения так,
# чтобы не возникала ошибка

s = str(123)
# Проверте, что тип значения в перменной s является str:
assert type(s) == __


text = "Hello World!"

# Проверте, что тип text является str:
assert __ == str

assert __ == text[1]
assert __ == text[3:5]
assert __ == text[6:]
assert __ == text[:6]
assert __ == text[:]
assert __ == text[-2]
assert __ == text[:5:-1]
assert __ == text[::3]
assert __ == text[:-7]
assert __ == text[3:-7]
assert __ == text[-3:-1]

# объединение строк
hi = "Hello, "
there = "world"
string = hi + there

assert __ == hi
assert __ == there
assert __ == string

# повторение строк
assert __ == text[:2]*3
