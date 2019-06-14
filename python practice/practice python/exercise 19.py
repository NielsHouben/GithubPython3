def numInList(lista, n):
    if n in lista:
        return True
    return False

a = [5, 7, 8, 19]
b = 7

if numInList(a, b):
    print("True")
else:
    print("False")