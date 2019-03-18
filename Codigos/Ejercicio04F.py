# -*- coding: utf-8 -*-
#Funciones del ejercicio 4

def cajero (x) :
    b = [5000,4000,3000,2000]
#son las variables de los billetes de 500, 200, 100 y 50 respectivamente
    m = [5000,4000,3000]
#son las variables de las monedas de 10, 5 y 1 respectivamente
    a = 0
    while x >= 500 :
        r = x%500
        n = x/500
        b[0] = b[0]-n
        a = a + n
        print n,
        print "billete(s) de $500"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    while x >= 200 :
        r = x%200
        n = x/200
        b[1] = b[1]-n
        a = a + n
        print n,
        print "billete(s) de $200"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    while x >= 100 :
        r = x%100
        n = x/100
        b[2] = b[2]-n
        a = a + n
        print n,
        print " billete(s) de $100"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    while x >= 50 :
        r = x%50
        n = x/50
        b[3] = b[3]-n
        a = a + n 
        print n,
        print " billete(s) de $50"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    while x >= 10 :
        r = x%10
        n = x/10
        m[0] = m[0]-n
        a = a + n
        print n,
        print " moneda(s) de $10"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    while x >= 5 :
        r = x%5
        n = x/5
        m[1] = m[1]-n
        a = a + n
        print n,
        print " moneda(s) de $5"
        if a > n :
            break
        if r != 0 :
            cajero (r)
    if x >= 1 :
        n = x/1
        m[0] = m[0]-n
        print n,
        print " moneda(s) de $1"

