# A program to give the students their grade based on test results
print("ENTER STUDENT ID: ")
id = int(input())

print("ENTER EXAM MARK: ")
exam = int(input())

print("ENTER ALL TEST RESULTS: ")
score1 = int(input())
score2 = int(input())
score3 = int(input())

sum = score1 + score2 + score3

tavge = sum / 3.0

final_score = 0.4 * tavge + 0.6 * exam

if (exam or score1 or score2 or score3) > 100:
    print("invalid value entered, please input scores from 0...100")
elif 90 <= final_score <= 100:
    print("your final score is: " + str(final_score))
    print("grade = 'A'")
    print("COMMENT:            Excellent!")
elif 80 <= final_score <= 89:
    print("your final score is: " + str(final_score))
    print("grade = 'B'")
    print("COMMENT:            Good")
elif 70 <= final_score <= 79:
    print("your final score is: " + str(final_score))
    print("grade = 'C'")
    print("COMMENT:            Okay")
elif 60 <= final_score <= 69:
    print("your final score is: " + str(final_score))
    print("grade = 'D'")
    print("COMMENT:            Needs Improvement")
else:
    print("your final score is: " + str(final_score))
    print("grade = 'F'")
    print("COMMENT:            Fail")
    print("You may re-enter next year")
