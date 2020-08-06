# Write your code here :-)
m = 0
st =""
finished = False
while not finished:
    print("Enter a line of txt (return to finish): ", end = "")
    s = input()
    if s != "":
        if len(s) > m:
            m = len(st)
            st = str(s)
    else:
        finished = True
print("longest string " + str(st))
print("number of characters: " + str(m))
