a = int(input("enter a number: "))

x = 1

divisorList=[]

while x != a:
    if a % x == 0:
        divisorList.append(x)  
    x = x + 1

print(divisorList,'are the divisors of', a)
