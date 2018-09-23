#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 12:04:44 2018

@author: alexanderrazzhivin
"""

READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

guest = READ                    # 001
user  = READ | WRITE            # 011
admin = READ | WRITE | EXECUTE  # 111

vasya = guest
assert 1 == (vasya & READ)
assert 0 == (vasya & WRITE)
assert 0 == (vasya & EXECUTE)