# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


# Даны три слова. Напечатать неповторяющиеся в них буквы.

if __name__ == '__main__':
    inp_text = str(input("Введите три слова через пробел> "))
    if inp_text.count(' ') != 2:
        print("ВВЕДИТЕ ПОЖАЛУЙСТА ТРИ СЛОВА ЧЕРЕЗ ПРОБЕЛ!!", file=sys.stderr)
        exit(1)
    inp_text = inp_text.replace(' ', '')
    inp_text = inp_text.lower()
    k = len(inp_text)
    temp = ""

    while k > 0:
        k = k - 1
        if inp_text.count(inp_text[k]) == 1:
            temp += inp_text[k]

    print("Буквы которые не повторялись в трех словах - " + temp)
