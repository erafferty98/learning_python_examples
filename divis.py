# two integer input, if int1 divisble by int2 "Y" else "N" if int2 = 0 "cannot divide"
int1 = 0
int2 = 0
int3 = 0
print ("input first integer")
int1 = int(input())
print ("input second integer")
int2 = int(input())

if int2 == 0:
    print("Cannot divide by zero")
elif int1 % int2 == 0:
    int3 = int1 // int2
    print("first number divided by second = " + str(int3))
else:
    print("cannot divide those numbers")
