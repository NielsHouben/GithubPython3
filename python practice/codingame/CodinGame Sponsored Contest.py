# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()] #Width, Height
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()] #start pos

x = x0
y = y0

jumpX = 1
jumpY = 1




# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)



    if bomb_dir == "U":
        y -= jumpY
    if bomb_dir == "UR":
        x += jumpX
        y -= jumpY
    if bomb_dir == "R":
        x += jumpX
    if bomb_dir == "DR":
        x += jumpX
        y += jumpY
    if bomb_dir == "D":
        y += jumpY
    if bomb_dir == "DL":
        x -= jumpX
        y += jumpY
    if bomb_dir == "L":
        x -= jumpX
    if bomb_dir == "UL":
        x -= jumpX
        y -= jumpY
        

    # the location of the next window Batman should jump to.
    print(x, y) 