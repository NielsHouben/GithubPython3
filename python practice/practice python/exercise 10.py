a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

lista = []



for elem in a:
    if elem in b and elem not in lista:
        lista.append(elem)

print(lista)


#print(set(a) & set(b))


# print(lista.append([element for element in a if element in b and element not in lista]))



# lista = []

# lista = [elem for elem in a if elem in b and elem not in lista]

# print(lista)

# print([lista.append(elem) for elem in a if elem in b and elem not in lista])

# print(lista)


# for elem in a:
#     if elem in b and elem not in lista:
#         lista.append(elem)

# print(lista)




# print([elem for elem in a if elem % 2 == 0])

# print(set(a) & set(b))
