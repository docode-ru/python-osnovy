# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения так,
# чтобы не возникала ошибка

a = 2
b = 3

assert 1 + 3 == 4
assert 3 * 3 == 9
assert 3 ** 2 == 9
assert 9 / 3 == 3
assert 6 - 3 == 3

assert 5 == a + b
assert -1 == a - b
assert 6 == a * b
assert 2.5 == 5 / a
assert 2 == 5 // a
assert 6 == 5 + b - a
assert 8 == a ** b
assert 5 ** 3 == 125
assert 0 == a*10 % 2
assert 1 == b*5 % 2

# Измените приоритет расставив скобки
assert 50 == (a + b) * 10
assert 15 == -1 * (a - 6) * 3 + b
