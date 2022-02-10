#Finance.py
#Mitchell McCulley
#Date: 02/01/2022

def finance():
    print("How much are you going to have in 10 years?")
    principal=eval(input("How much did you deposit in the bank?:"))
    rate=eval(input("What is the interest rate?:"))

    for i in range(10):
        principal=principal*(1+rate)
    print("You will have $:", principal,"in 10 years")

finance()
