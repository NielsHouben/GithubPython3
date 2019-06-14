open_file = open("namn.txt", "r")
a = open_file.read()
open_file.close()

def removeDup(a):
    return list(set(a))

namn = []
word = ""
for elem in a:
    if elem.isupper():
        namn.append(word)
        word = elem
    else:
        word += elem

namn.remove("")
nynamn = []

for i in namn:
    a = []
    for o in i:
        a.append(o)
    a.pop()
    nynamn.append("".join(a))

namn1 = removeDup(nynamn)

for elem in namn1:
    a = 0
    for o in nynamn:
        if elem == o:
            a += 1
    print("{}: {}".format(elem, a))