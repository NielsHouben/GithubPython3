print("")
print("")
lista = [5, 5, 8, 13, 15, 20, 20, 17]

def removeDupLoop(a):
    p = []
    for elem in a:
        if elem not in p:
            p.append(elem)

    return p

print("{} was made with a for loop adding element by element if not already added".format(removeDupLoop(lista)))
print("")


def removeDupSet(a):
    return list(set(a))

print("{} was made by converting the list to a set and back, sets can't hold duplicates".format(removeDupSet(lista)))

# def removeDup(a):
#     b = a[:]
#     return(set(a) & set(b))

# sets store stuff in a numeretic order!



print("")
print("")