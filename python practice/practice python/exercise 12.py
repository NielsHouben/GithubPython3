a = [5, 10, 15, 20, 25, 30, 35, 40]

def firstLast(clone):
    taBort = clone[1:len(clone) -1]

    for elem in taBort:
        clone.remove(elem)

    return clone

print(firstLast(a))


def first(aList):
    toDelI = aList[1: len(aList)-1]
    return [element for element in aList if element not in toDelI]

print(first(a))
# deras lösning
# def list_ends(a_list):
# return [a_list[0], a_list[len(a_list)-1]]

# def firstLastTwo(aList):    
#     del aList[1: len(aList) -1 ]
# print(a)
     

# print([elem for elem in a if elem % 2 == 0])



# plats = 1
#     for i in lista:
#         obj = lista[plats]
#         lista.remove(obj)  
#         plats += 1
