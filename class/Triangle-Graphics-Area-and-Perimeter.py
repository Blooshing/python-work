from graphics import*
from math import*
def main():
    win=GraphWin("Triangle",400,400)
    win.setCoords(-10,-10,10,10)
    
    message=Text(Point(0,8), "Click on the first point").draw(win)
    p1=win.getMouse()
    p1.draw(win)

    message.setText("Click on the second point")
        
    p2=win.getMouse()
    p2.draw(win)

    message.setText("Click on the third point")
    p3=win.getMouse()

    triangle=Polygon(p1,p2,p3)
    triangle.draw(win)
    triangle.setFill("light green")
    
    x1=p1.getX()
    y1=p1.getY()
    x2=p2.getX()
    y2=p2.getY()
    x3=p3.getX()
    y3=p3.getY()

    a=sqrt((x1-x3)**2+(y1-y3)**2)
    b=sqrt((x2-x3)**2+(y2-y3)**2)
    c=sqrt((x1-x2)**2+(y1-y2)**2)

    s=(a+b+c)/2

    area=sqrt(s*(s-a)*(s-b)*(s-c))
    perimeter=(a+b+c)
    
    message.setText("The area is: "+str(round(area,2)))
    
    message1=Text(Point(0,7), "The Perimeter is: "+str(round(perimeter,2)))
    message1.draw(win)

    messageClose=Text(Point(0,6),"Click to close the window")
    messageClose.draw(win)
    win.getMouse()
    win.close()
main()
