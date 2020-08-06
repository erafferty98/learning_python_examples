# x1
total = 0
finished = False
while not finished:
    print("Please enter a number (end with 0):")
    s = input()
    num = int(s)
    if num != 0:
        total = total + num
    else:
        finished = True
print("Total is " + str(total))
