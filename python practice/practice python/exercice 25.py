import random

print("Think of a number between 1 and 100")
print("")

guesses = 0
l = 1
h = 100
while True:
    guesses += 1
   

    print("l: ", l)
    print("h: ", h)


    g = random.randint(l, h)
    
    #break if only one number is guessable
    if l == h:
        break
    while True:
    
        hl = input("is {} Too high/low or your number(high, low, my number): ".format(g))
        if hl == "high":
            # "Guess lower"
            h = g - 1
            break

        elif hl == "low":
            # "Guess higher"
            l = g + 1
            break


        elif hl == "my number":
            break
    print("")
    if hl == "my number":
        break

    
print("{} is your number".format(g))
print("It took me {} guesses to guess your number".format(guesses))