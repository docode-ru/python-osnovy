# -*- coding=utf-8 -*-

__ = False

# Задание
# Замените __ на соответствующие значения и
# исправьте все ошибки

a = 4       # бинарное 100
b = 5       # бинарное 101

assert __ == a & b
assert __ == a | b
assert __ == a ^ b
assert __ == ~a
assert __ == ~(a-1)
assert __ == a >> 1
assert __ == b << 2


READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

guest = READ                    # 001
user  = READ | WRITE            # 011
admin = READ | WRITE | EXECUTE  # 111

vasya = guest
assert __ == (vasya & READ)
assert __ == (vasya & WRITE)
assert __ == (vasya & EXECUTE)