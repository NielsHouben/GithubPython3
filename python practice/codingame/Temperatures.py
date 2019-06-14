n = int(input())
lst = []
lst2 = []

for i in input().split():
    t = int(i)
    
    lst.append(t)
    
    lst2.append(abs(t))

p = 0
for elem in lst2:
    if elem == min(lst2):
        
        if elem != abs(elem):
            if abs(elem) not in lst:
                break
        if elem == abs(elem):
            break
    
    
    p += 1

print(lst[p])







# n = int(input())
# lst = []
# lst2 = []

# for i in input().split():
#     t = int(i)
    
#     lst.append(t)
    
#     lst2.append(abs(t))
    
# p = 0
# for elem in lst2:
#     if elem == min(lst2):
#         break
#     p += 1

# print(lst[p])