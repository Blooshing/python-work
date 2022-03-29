def main():
    infile = open('students.txt', 'r')

    counter = 0
    total = 0.0

    infile.readline()

    for line in infile:
        counter = counter+1

        print(line)

        first, last, grade = line.split()
        total = total + eval(grade)
    print("The average grade is:", total/counter)
main()
