def drawLine(length):
    return ("".join(["-" for i in range(length)]))

def drawLineWidth(width, lineLength):
    return ("".join([" " + drawLine(lineLength) for i in range(width)]))

def drawH(width, lineLength):
    H = ""
    for i in range(width + 1):
        H += "|"
        for i in range(lineLength):
            H += " "
    return(H)

def drawGameBoard(W, H):
    print(drawLineWidth(W, 3))

    for i in range(H):
        print(drawH(W,3))
        print(drawLineWidth(W, 3))

drawGameBoard(3, 3)


# drawGameBoard("".join([input("Width and Height: ").split()]))

# drawGameBoard(input("Width and Height: ").split())