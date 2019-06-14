import time
def checkDivisors(a):
    x = 1

    divisorList=[]

    while x != a:
        if a % x == 0:
            divisorList.append(x)  
        x = x + 1
    
    return divisorList

def getInteger():
    return int(input("Enter a number: "))

# num = getInteger()

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for elem in prime:
    num = elem

    if checkDivisors(a = num) == [1]:
        print("{} is a prime number".format(num))

    time.sleep(0.1)
