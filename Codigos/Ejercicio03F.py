# -*- coding: utf-8 -*-
#Funciones del ejercicio 3


def ubicacion (letrita, palabrita):
    '''Verifica si una letra se encuentra
dentro de una cadena'''
    P = list(palabrita)
    for i in range(len(P)): 
        for P[i] in P:
            if letrita == P[i]:
                return True


def posicion (letrita, palabrita):
    '''Verifica en qué posición se encuentra
una letra dentro de una cadena'''
    P = list(palabrita)
    j = 0
    for i in range(len(P)):
        j = i+1
        for P[i] in P:
            if letrita == P[i]:
                print P[i]+" corresponde a la posicion ",
                return j 

def palabritas (palabrita1,palabrita2):
    ''''''
    p1 = palabrita1.lower()
    p2 = palabrita2.lower()
    #pasa las cadenas a minúsculas 
    P1 = list (p1)
    P2 = list (p2)
    #convierte las cadenas en una lista
    if len(P1) == len(P2):
    #ve si tienen el mismo número de letras
        for i in range(len(P1)):
            for P1[i] in P1 :
                if ubicacion (P1[i],P2) :
                    return "Es posible"
                else :
                    return "No es posible"
    else:
        return "No es posible"

def posicion 
