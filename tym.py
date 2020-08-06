# time response
print("please enter the time in 4-digit integer (military) form")
time = int(input())

if 2400 <= time < 0:
    print("invalid time")
elif 1800 < time < 2400:
    print("good evening")
elif 1200 < time <= 1800:
    print("good afternoon")
elif 500 < time <= 1200:
    print("good morning")
elif 0 < time <= 500:
    print("why are you awake")
