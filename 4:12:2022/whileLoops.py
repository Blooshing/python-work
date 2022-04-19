def main():
    moredata = "yes?"
    total = 0.0 
    count = 0
    
    while moredata == "yes?":
        score = eval(input("Enter a score: "))
        total = total +score
        count = count+1
        moredata = input("Do you still have data? (Yes or no?): ")
    average = total/count
    
    print("The average of the data is:", average)
    
main()