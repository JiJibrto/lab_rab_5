# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string

if __name__ == '__main__':
    in_text = str(input("Введите строку хотя ы с одной запятой> "))
    if in_text.count(',') == 0:
        print("Запятых нет, а смысл тогда в этом модуле???", file=sys.stderr)
        exit(1)

    temp_a = in_text.find(',')
    temp_b = in_text.find(',', temp_a+1)

    if temp_b == -1:
        print(in_text[temp_a+1:])
    else:
        print(in_text[temp_a+1:temp_b])