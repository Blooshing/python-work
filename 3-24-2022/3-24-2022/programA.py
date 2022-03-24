#Write your data to a file.
def main():
   fname = input("Enter the output filename: ")
   outfile = open(fname,'w')
   name=input("Enter your name: ") 
   major=input("What is your major: ")
   print("This is the file that was created for you!!!\nYour name is:",name,"\nYour major is:", major, file=outfile)
  
   outfile.close()

main()
