# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения так,
# чтобы не возникала ошибка

a = 2
b = 3

assert 1 + 3 == __
assert 3 * 3 == __
assert 3 ** 2 == __
assert 9 / 3 == __
assert 6 - 3 == __

assert __ == a + b
assert __ == a - b
assert __ == a * b
assert __ == 5 / a
assert __ == 5 // a
assert __ == 5 + b - a
assert __ == a ** b
assert __ ** 3 == 125
assert __ == a*10 % 2
assert __ == b*5 % 2

# Измените приоритет расставив скобки
assert 50 == a + b * 10
assert 15 == -1 * a - 6 * 3 + b
