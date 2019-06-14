n = "number"
div = "divide"
while str.isdigit(n) == False:
    n = input("Enter a number: ")
    if str.isdigit(n) == False:
        print("Your number should only contain digits")
n = int(n)
while str.isdigit(div) == False:
    div = input("Divide your number by: ")
    if str.isdigit(div) == False:
        print("You can only divide with digits")
div = int(div)

if n % div == 0:
    print("You can divide", n, ", with ", div)
else:
    print(n, "can't be divided by", div)


# m = n / div

# m = int(m)

# m = m * div

# if m == n:
#     print("You can divide", n, ", with ", div)
# else:
#    print(n, "can't be divided by", div)
