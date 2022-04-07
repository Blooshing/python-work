#grades
def main():
    testGrade = eval(input("Please input the test grade of the student: "))

    if testGrade >= 90:
        print("The student got an A")
    elif testGrade >= 80:
        print('The student got a B')
    elif testGrade >= 70:
        print('The student got a C')
    elif testGrade >= 60:
        print("The student got a D")
    elif testGrade <= 60:
        print('The student failed the exam')
main()
