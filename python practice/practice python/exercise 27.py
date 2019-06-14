print("\n" * 50)

gameBoard = \
       [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]

import time



P = "P1"
turns = 0
while turns < 9:
        #Print game board
        for i in range(3):
                print(gameBoard[i])
        print()

        row = 0
        col = 0

        while True:
                inp = input("{}, make your turn on row x and column y (x, y): ".format(P))
                break
                print("Invalid input, try again")
        
        inp = inp.split(", ")

        row = int(inp[0]) - 1
        col = int(inp[1]) - 1

        PC = "X"

        gameBoard[row][col] = PC



        #p1, P = P1, PC = X
        #p2, P = P2, PC = O

