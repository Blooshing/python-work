from math import*
def area():
    a=eval(input("Please enter in side A's length"))
    b=eval(input("Please enter in side B's length"))
    c=eval(input("Please enter in side C's length"))
    s=(a+b+c)/2
    Area=sqrt((s*(s-a)*(s-b)*(s-c)))
    print("The area of the triangle is:", Area)
area()
