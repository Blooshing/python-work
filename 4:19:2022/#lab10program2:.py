#lab10program2: 
def main(): 
    creditsEarned = eval(input("How many credits do you have?: "))
    
    if creditsEarned < 7: 
        print ("They are a freshman.")
    elif creditsEarned >=7 and creditsEarned < 16:
        print("They are a sophomore")
    elif creditsEarned >=16 and creditsEarned < 26: 
        print("They are a junior.")
    elif creditsEarned >= 26: 
        print("They are a senior.")
main()
        