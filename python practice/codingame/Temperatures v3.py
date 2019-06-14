inp = input()

# if inp 


Temperatures = []

for i in input().split():
    t = int(i)
    Temperatures.append(t)





pos = []
neg = []
for t in Temperatures:
    if t == abs(t):
        pos.append(t)
    else:
        neg.append(abs(t))

if pos != []:
    if min(pos) <= min(neg):
        print(min(pos))
elif neg != []:
    print(min(neg) - min(neg) - min(neg))
else:
    print(0)