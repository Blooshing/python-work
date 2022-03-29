def main():
    studentCount = eval(input("How many students do you have?: "))
    outfile = open('students.txt', 'w')
    print("{0}\t\t{1}\t\t{2}".format("First","Last", "Grade"), file=outfile)
    
    for i in range(studentCount):
        firstname = input("What is the first name of the student?: ")
        lastname = input("Enter the last name of the student: ")
        grade = eval(input("Enter the grade of the student: "))

        print("{0}\t\t{1}\t\t{2}".format(firstname,lastname, grade), file=outfile)

    

    
main()
