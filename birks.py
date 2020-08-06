#count number of Birks in sequence given
finished = False
m = 0
s = ""
while not finished:
    s = input()
    if s[0:4] == "Birk":
        m = m + 1
    elif s == "":
        finished = True
print("number of Birks " + str(m))

