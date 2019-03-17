# -*- coding: utf-8 -*-
#Funciones del ejercicio 2

def orden_l (x) :
    '''Ordena una lista de mayor a menor'''
    for i in range(len(x)-1,0,-1): #te da una lista volteada con los índices de la entrada
        for j in range(i) :
            if x[j]<x[j+1]: #aquí compara los elementos uno por uno
                t = x[j]    #y esto los intercambia si uno es mayor que el otro
                x[j] = x[j+1] 
                x[j+1] = t
    return (x) 

def triangulo(n):
    for x in range (1,n+1):
        print x*"*"

def trian_inv (n):
    L = range (1,n)
    L1 = orden_l (L)
    for x in L1 :
        print x*"*"
