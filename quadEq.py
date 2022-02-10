#Quadratic Equation
#Mitchell McCulley
#02.01.2022

print("This is the code to run the quadratic equation program")
print("Best of luck :)")
#Begin:
from math import*
def quadEq():
    print("This is the code for the quadratic equation") 
    a=eval(input("Enter in the first coefficient of the first term:"))
    b=eval(input("Enter the coefficient of the second term:"))
    c=eval(input("Enter the coefficient of the third term:"))

    root1= (-b+sqrt(b**2-4*a*c))
    root2= (-b-sqrt(b**2-4*a*c))

    print("The roots are:",root1,"and", root2)
quadEq()
