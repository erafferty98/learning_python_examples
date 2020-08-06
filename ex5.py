# tests lengths of lines before previous are longer
l1 = ""
l2 = ""
fin = True
print("enter the first line")
l1 = str(input())
while fin is True:
    print("enter the next line")
    l2 = str(input())
    if l2 != "":
        if len(l1) > len(l2):
            print("Yes")
        elif len(l1) < len(l2):
            print("No")
        else:
            print("No")
        l1 = l2
    else:
        fin = False
