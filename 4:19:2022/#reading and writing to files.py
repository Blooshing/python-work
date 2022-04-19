#reading and writing to files
def main():
    infile = open("students.txt", 'r')
    outfile = open("outStudents.txt", 'w')
    
    for line in infile:
        first, last, grade = line.split()
        newGrade = 1.05 * eval(grade)
        
        print(first, last, newGrade, file = outfile)
    infile.close()
    outfile.close()

main()