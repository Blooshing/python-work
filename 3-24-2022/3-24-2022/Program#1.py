def main():
    print ("This program creates a file of names of the users")
    # get the file names
    fileName = input("Enter a file name that you need to create:  ")
    # open the files
    ofile = open(fileName, 'w')
    n = eval(input("Enter the number of users: "))
    for i in range(n):
	    name = input("Please enter the first name and the last name separated by a space:  ")
	    print(name, file= ofile)

    print("\n Thank you … all the names were written to the file .")
    ofile.close()
main()
