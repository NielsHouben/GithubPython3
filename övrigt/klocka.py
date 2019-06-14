import time

s = "sekunder"
m = "minuter"
h = "timmar"

s = 0

while str.isdigit(h) == False:
    h = input("hut många timmar har gått: ")
    if str.isdigit(h) == False:
        print("Antal timmar tar bara emot siffror")
h = int(h)

while str.isdigit(m) == False:
    m = input("hut många minuter har gått: ")
    if str.isdigit(m) == False:
        print("Antal minuter tar bara emot siffror")
m = int(m)

while True:
    print(h,":",m,":",s)
    time.sleep(1)
    s += 1
    if s == 60:
        m = m + 1
        s = 0
    if m == 60:
        h = h + 1
        m = 0
    if h == 24:
        h = 0