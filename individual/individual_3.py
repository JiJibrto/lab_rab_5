# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# Путем вставок и удаления символов исправить ошибки:
# в слове прроцесор;
# во фразе теекстовыйфайл;
# во фразе програма и аллгоритм;
# во фразе процесор и паммять.

if __name__ == '__main__':
    inp_text = str(input("Введите слово для исправления> "))

    if inp_text == "прроцесор":
        inp_text = inp_text[:inp_text.find('р')]+inp_text[inp_text.find('р')+1:inp_text.find('с')+1]\
                   + inp_text[inp_text.find('с'):]
    elif inp_text == "теекстовыйфайл":
        inp_text = inp_text[:inp_text.find('е')]+inp_text[inp_text.find('е')+1:inp_text.find('й')+1]\
                   + " " + inp_text[inp_text.find('й')+1:]
    elif inp_text == "програма и аллгоритм":
        inp_text = inp_text[:inp_text.find('м')+1]+inp_text[inp_text.find('м'):inp_text.find('л')]\
                   + inp_text[inp_text.find('л')+1:]
    elif inp_text == "процесор и паммять":
        inp_text = inp_text[:inp_text.find('с')+1]+inp_text[inp_text.find('с'):inp_text.find('м')]\
                   + inp_text[inp_text.find('м')+1:]
    else:
        print("Я не ИИ и работаю только с заготовленными инпутами(", file=sys.stderr)
        exit(1)

    print("Исправоенное предложение> "+inp_text)
