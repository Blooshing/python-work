def slopeFunction():
    x_1=eval(input("What is x1?:"))
    x_2=eval(input("What is x2?:"))
    y_1=eval(input("What is y1?:"))
    y_2=eval(input("What is y2?:"))
    slope=(y_2-y_1)/(x_2-x_1)
    print("The slope of the line is:",slope)
slopeFunction()
from math import*
def distanceFunc():
    x_1=eval(input("What is x1?:"))
    x_2=eval(input("What is x2?:"))
    y_1=eval(input("What is y1?:"))
    y_2=eval(input("What is y2?:"))
    distance=sqrt(((x_2-x_1)**2)+((y_2-y_1)**2))
    print("The distance is:",distance)
distanceFunc()
                  
