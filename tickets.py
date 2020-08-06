# selling tickets in batches of up to 4 until all sold out
t = 0
tl = 200
num1 = 0
c = 0
fin = True
while fin is True:
    num1 = min(4, int(tl))
    print(str(tl) + " tickets remaining")
    print("How many do you want to buy?")
    print("Minimum 1, maximum " + str(num1))
    t = int(input())
    c = c + 1
    if num1 != 0:
        tl = tl - t
        if tl == 0:
            fin = False
            print(str(c) + " sales transactions")
