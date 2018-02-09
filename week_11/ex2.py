# -*- coding: utf-8 -*-
import string
import sys
import unicodedata

def maiusculas(a_string):
    uppers = ""
    for c in a_string:
        if c in string.ascii_uppercase:
            uppers = uppers + c
    return uppers

def menor_nome(names_array):
    
    if len(names_array) > 0:
        sizes = []
        minimum = sys.maxsize
        index = 0

        for name in names_array:
            raw = unicodedata.normalize("NFKD", name.replace(" ", "")).encode("ASCII","ignore")
            sizes.append(len(raw))

        for i,value in enumerate(sizes):
            if value < minimum:
                minimum = value
                index = i
        print(sizes)
        return names_array[index].capitalize()
    else:
        return ""

print(maiusculas('Programamos em python 2?'))
# deve devolver 'P'
print(maiusculas('Programamos em Python 3.'))
# deve devolver 'PP'
print(maiusculas('PrOgRaMaMoS em python!'))
# deve devolver 'PORMMS'
print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))