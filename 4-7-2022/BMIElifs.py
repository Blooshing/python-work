#BMI

#bmi = (weight(LBs)*720)/(height**2)
def main():
    

    weight = eval(input("Please enter your weight: "))
    height = eval(input("Please enter your height: "))

    bmi = (weight*720)/(height**2)

    if bmi >= 19 and bmi <= 25:
        print("You are in a 'healthy range'")
    elif bmi <19:
        print("You are below the average")
    elif bmi >25:
        print("You are above the average")
main()
        
    
