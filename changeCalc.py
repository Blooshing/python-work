#Change Calculator.py
#Mitchell
#02/01/2022

def changeCalc():
    quarters=int(input("Enter the number of quarters:"))
    nickels=int(input("Enter the number of nickels:"))
    dimes=int(input("Enter the number of dimes:"))
    pennies=int(input("Enter the number of pennies:"))

    total=quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    print("The total is $", total)
changeCalc()
