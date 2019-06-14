#password generator
import string
import random
print("")

# returns random number 1-9
def randomDigit():
    return (random.randint(1, 9))
# e.g print(randomDigit())

# prints a random letter (if given lower, the lowercase and viseversa with upper)
def randomLetter(caps):
    if caps == "lower":
        alphabet = list(random.choice([string.ascii_lowercase]))
    elif caps == "upper":
        alphabet = list(random.choice([string.ascii_uppercase]))

    return (random.choice(alphabet))
# e.g print(randomLetter("upper"))
# e.g print(randomLetter(random.choice(["lower", "upper"])))

# Removes duplicates from list input
def removeDup(a):
    return list(set(a))

# OBS!
# THINGS TO ADD (ask if lowercase, uppercase, numbers should be allowed)
while True:
    print("Settings:")
    totalLen = "Not a digit"
    while str.isdigit(totalLen) == False:
        totalLen = (input("Password Length (digit): "))
        if str.isdigit(totalLen) == False:
            print("Password length should only contain digits!")
    totalLen = int(totalLen)

    allowDup = input("Allow duplicates (no, else means yes): ").upper()

    while True:
        password = []
        for i in range(0, totalLen):
            password.append(random.choice([(randomLetter(random.choice(["lower", "upper"]))), (randomDigit())]))
        
        print("")

        
        if allowDup == "NO":
            
            password = removeDup(password)
            while totalLen != len(password):
                password.append(random.choice([(randomLetter(random.choice(["lower", "upper"]))), (randomDigit())]))
                
                if len(password) != totalLen:
                    password = removeDup(password)
            

        #prints password as a string not as a list
        print("Your password: {}".format("".join(str(elm) for elm in password)))


        ask = input("type settings to channge them, x to leave, else generates a new password: ").upper()

        if ask == "SETTINGS" or ask == "X":
            break
    
    print("")

    if ask == "X":
        break







# import string
# import random

# def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
# 	return ''.join(random.choice(chars) for _ in range(size))

# print(pw_gen(int(input('How many characters in your password?'))))