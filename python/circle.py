from graphics import*
from math import*

def main():
    win=GraphWin("Circle", 400, 400)
    win.setCoords(-10,-10,10,10)

    r=eval(input("Enter the radius: "))
    y=eval(input("Enter the y-intercept: "))

    circle=Circle(Point(0,0), r).draw(win)
    line=Line(Point(-10,y), Point(10,y)).draw(win)
    x=sqrt(r**2-y**2)
    print("the two intersection points are(", x,",", y,") and"
          "(", -x,",",y,")")
    c1=Circle(Point(x,y), 0.25).draw(win)
    c1.setFill("red")

    c2=c1.clone()
    c2.move(-2*x, 0)
    c2.draw(win)
    
main()
