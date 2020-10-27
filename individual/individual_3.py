# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string

# Путем вставок и удаления символов исправить ошибки:
# в слове прроцесор;
# во фразе теекстовыйфайл;
# во фразе програма и аллгоритм;
# во фразе процесор и паммять.

if __name__ == '__main__':
    inp_text = str(input("Введите слово для исправления> "))

    if inp_text == "прроцесор":
        inp_text = inp_text[:2]+inp_text[3:6]+'c'+inp_text[6:]
    elif inp_text =="теекстовыйфайл":
        inp_text = inp_text[:1]+inp_text[2:10]+" "+inp_text[10:]
    elif inp_text == "програма и аллгоритм":
        inp_text = inp_text[:7]+'м'+inp_text[7:12]+inp_text[13:]
    elif inp_text == "процесор и паммять":
        inp_text = inp_text[:6]+'c'+inp_text[6:14]+inp_text[15:]
    else:
        print("Я не ИИ и работаю только с заготовленными инпутами(", file=sys.stderr)
        exit(1)

    print("Исправоенное предложение> "+inp_text)
