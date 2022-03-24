def main():
    studentCount = eval(input("How many students do you have?: "))

    for i in range(studentCount):
        name = input("What are the names of the students?: ")

    print("{0}\t\t{1}".format("Name", "Grade"))

    outfile = open("students.txt", 'w')
main()
