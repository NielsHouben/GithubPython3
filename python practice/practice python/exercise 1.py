name = input("enter your name: ")
a = "age"
b = "repeat message"

while str.isdigit(a) == False:
    a = input("Enter your age: ")
    if str.isdigit(a) == False:
        print("Your age should only contain digits")
a = int(a)
a = 100 - a

print(name, ", you will be 100 years old in", 2019 + a)

while str.isdigit(b) == False:
    b = input("give me another number:  ")
    if str.isdigit(b) == False:
        print("Your other number should only contain digits")
b = int(b)

for b in range(0, b):
    print(name, ", you will be 100 years old in", 2019 + a)




