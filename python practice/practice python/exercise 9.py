import random

print("welcome to the guessing game, type exit at any time to exit")

u = "userInput"
r = 10

while True:
    g = 0
    r = random.randint(1, 9)
    while u != r and u != "exit":
        g = g + 1
        while True:
            u = input("Enter your guess: ")
            if u == "exit":
                break      
            try:
                u = int(u)
                break
            except ValueError:
                print("Your guess should only contain digits or be exit")
    if u == "exit":
        break
    print("{} was correct, it took you {} tries".format(u, g))
    if input("Type anything to replay, type exit to leave: ") == "exit":
        break
