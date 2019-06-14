import time

antal = int(input("How many numbers do you want in the sequence: "))

antalGjorda = 0

n = 0
l = 1
k = 0

while antalGjorda != antal:
    time.sleep(0.1)
    print(n)
    n = l + k
    k = l
    l = n
    
    antalGjorda += 1


# nån annans
# total = int(input("How many? "))
# numfib = [0, 1]
# for i in range(1, total):
#  numfib.append(numfib[i] + numfib[i-1])
# print(numfib[1:total+1])
