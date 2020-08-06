# are you in the higher tax bracket
print('this program outputs total salary so you know your tax bracket')
print('input first salary')
salary1 = int(input())
print('input second salary')
salary2 = int(input())

comb= salary1 + salary2
if int(comb) > 40000:
    print("you're in the higher tax bracket with a combined salary of " + str(comb))
else:
    print("you are in the lower tax bracket with a combined salary of " + str(comb))


