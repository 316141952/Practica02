# -*- coding: utf-8 -*-
#Función del ejercicio 1

def rectangulo (a,b) :
#a es la altura y b es la base
    '''Dando una base y una altura,
te devuelve un rectángulo con *'''
    L = range(b)
    j = 0
    while j < a :
        for i in range(len(L)) :
            print '*',
        j = j + 1
        print '\n'

