# Write your code here :-)
m = 0
finished = False
while not finished:
    print("Enter another integer number (0 to finish): ", end = "")
    s = input()
    if int(s) == 100:
        m = m + 1
    elif int(s) == 0:
        finished = True
print("number of 100's " + str(m))
