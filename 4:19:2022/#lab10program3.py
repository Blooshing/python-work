#lab10program3

def main(): 
    age, citizenship = eval(input("Please enter your age and how many years you've been a citizen: "))
    
    if age >= 30 and citizenship >= 9: 
        print("You are eligible for both positions.")
    elif age >= 25 and citizenship >= 7: 
        print("You are eligible for only the House of Representative position.")
    else: 
        print("You are uneligible for both positions.")
main()