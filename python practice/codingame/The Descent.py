# v1
import sys
import math

# game loop
while True:
    lista = []
    for elem in range(8):
        lista.append(int(input()))
    
    a = 0
    c = 0

    for elem in lista:
        if elem > a:
            a = elem
            cc = c
        c += 1

    print(cc)

# v2
import sys
import math

# game loop
while True:
    lista = []
    for elem in range(8):
        lista.append(int(input()))
    
    large = max(lista)
    
    c = 0
    for elem in lista:
        c += 1
        if elem == large:
            break

    print(c)

#v3
import sys
import math

# game loop
while True:
    lista = []
    for elem in range(8):
        lista.append(int(input()))
    
    m = max(lista)
    a = [i for i, j in enumerate(lista) if j == m]

    print(a[0])