slut = "hej"

while slut != "X":
    print("Sten-Sax-Påse, best av 3")
    p1p = 0
    p2p = 0   

    while True:
        p1 = "blank"
        p2 = "blank"
        
        while True:
            p1 = input("p1: ").upper()
            if p1 == "STEN":
                break
            elif p1 == "SAX":
                break
            elif p1 == "PÅSE":
                break
            print("Du kan bara välja sten, sax eller påse")
        while True:
            p2 = input("p2: ").upper()
            if p2 == "STEN":
                break
            elif p2 == "SAX":
                break
            elif p2 == "PÅSE":
                break
            print("Du kan bara välja sten, sax eller påse")

        if p1 == "STEN" and p2 == "SAX":
            p1p += 1
        elif p1 == "SAX" and p2 == "PÅSE":
            p1p += 1
        elif p1 == "PÅSE" and p2 == "STEN":
            p1p += 1

        if p2 == "STEN" and p1 == "SAX":
            p2p += 1
        elif p2 == "SAX" and p1 == "PÅSE":
            p2p += 1
        elif p2 == "PÅSE" and p1 == "STEN":
            p2p += 1

        if p1p == 2 or p2p == 2:
            break
        elif p1 != p2:
            print("player 1 har {} påäng".format(p1p))
            print("player 2 har {} påäng".format(p2p))
        elif p1 == p2:
            print("Lika, ingen fick poäng")

    if p1p == 2:
        print("player 1 vann med {} poäng".format(p1p))
        print("player 2 lförlorade med {} poäng".format(p2p))
    else:
        print("player 2 vann med {} points".format(p2p))
        print("player 2 förlorade med {} points".format(p2p))
    slut = input("Press enter to restart or type x to stop").upper()