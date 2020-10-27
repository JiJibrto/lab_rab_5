# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Дано предложение. Вывести все имеющиеся в нем буквосочетания нн.

if __name__ == '__main__':
    in_file = str(input("Введите предложение> "))
    in_file.lower()
    temp = 0

    temp = in_file.count('нн')

    if temp == 0:
        print("Буквосочетания \"нн\" не найденны")
    else:
        print(f"Количество буквосочетаний \"нн\" = {temp}")
