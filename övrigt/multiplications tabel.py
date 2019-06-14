diff = "difficulty"

while diff != "X":
    diff = input("Type Easy, hard or type x to go stop: ").upper()
    edone = 0
    while diff == "EASY":
        from random import *
        a = randint(1, 10)
        b = randint(1, 10)
        sa = "svara"
        sb = 1
        while True:
            sa = "svara"
            while str.isdigit(sa) == False:
                print(a,"*",b,"= ")
                sa = input().upper()

                if sa == "X":
                    print(edone)
                    diff = "dip"
            sa = int(sa)

            sb = a * b

            if sa == sb:
                edone += 1
                break
            




while diff == "HARD":
    print("Comming soon")




# from random import *
# x = randint(1, 100)
# print(x)