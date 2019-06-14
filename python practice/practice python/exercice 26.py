game = \
       [[2, 2, 2],
        [0, 2, 2],
        [2, 1, 0]]

#If no one has won, winner will stay as 0
winner = 0


#Won by 3 in row
for i in range(3):
    if game[i][0] == game[i][1] == game[i][2] != 0:
        winner = game[i][0]


#Won by 3 in collumn
for i in range(3):
    if game[0][i] == game[1][i] == game[2][i] != 0:
        winner = game[0][i]


#Won by 3 in diagonal
if game[0][0] == game[1][1] == game[2][2] != 0:
    winner = game[0][0]

if game[0][2] == game[1][1] == game[2][0] != 0:
    winner = game[0][2]

#Clear screan
print("\n" * 50)

#Print game board
for i in range(3):
    print(game[i])
print()

#Prints the winner
if winner == 0:
    print("Niether player won")
else:
    print("Player {} won".format(winner))






#Simple verision

# game = \
#     [[2, 2, 2],
# 	[0, 2, 2],
# 	[2, 1, 0]]

# winner = 0

# for i in range(3):
#     if game[i][0] == game[i][1] == game[i][2] != 0:
#         winner = game[i][0]

# for i in range(3):
#     if game[0][i] == game[1][i] == game[2][i] != 0:
#         winner = game[0][i]

# if game[0][0] == game[1][1] == game[2][2] != 0:
#     winner = game[0][0]

# if game[0][2] == game[1][1] == game[2][0] != 0:
#     winner = game[0][2]


# if winner == 0:
#     print("Niether player won")
# else:
#     print("Player {} won".format(winner))