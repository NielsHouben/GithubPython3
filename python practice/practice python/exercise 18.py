import random

f = 0
genNum = []
genNum = [random.randint(1, 9) for i in range(0, 4)]


while True:
    cow = 0
    bull = 0
    guess = [0]    
    four = "four"
    
    while len(guess) != 4:
        guess = input("Enter your {} digit guess: ".format(four))
        guess = [elem for elem in guess]
        guess = list(map(int, guess))
        four = "FOUR"
   
    for i in range(0, len(guess)):
        if guess[i] == genNum[i]:
            cow += 1
        elif guess[i] in genNum:
            bull += 1

    print("{} cows".format(cow))
    print("{} bulls".format(bull))
    
    f += 1

    if cow == 4:
        print("you guessed the number!")
        print("it was {}".format(genNum))
        print("it took you {} tries".format(f))
        break
