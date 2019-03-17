# -*- coding: utf-8 -*-
#Funciones del ejercicio 3


def ubicacion (letrita, palabrita):
    '''Verifica si una letra se encuentra
dentro de una cadena'''
    P = list(palabrita)
    for i in range(len(P)): 
        for P[i] in P:
            if letrita == P[i]:
                return 1
            else :
                return 0


print ubicacion ("p","perro")


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
                print j 


posicion ("p","perro")


def palabritas (palabrita1,palabrita2):
    p1 = palabrita1.lower()
    p2 = palabrita2.lower()
    #pasa las cadenas a minúsculas 
    P1 = list (p1)
    P2 = list (p2)
    #convierte las cadenas en una lista
    if len(P1) == len(P2):
        for i in range(len(P1)):
            for P1[i] in P1 :
                a = ubicacion(P1[i],P2)
                if a == 1:
                    return posicion(P1[i],P2)
                else :
                    return "No es posible"
    else:
        return "No es posible"
    

print palabritas ("Amar","Rama")



 
