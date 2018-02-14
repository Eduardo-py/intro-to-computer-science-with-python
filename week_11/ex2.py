# -*- coding: utf-8 -*-
import string
import sys
import unicodedata

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
        return names_array[index].capitalize()
    else:
        return ""

print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))