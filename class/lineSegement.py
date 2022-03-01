#program #4
#Mitchell McCulley
#March 1, 2022
from graphics import*
from math import*
def main():
    win=GraphWin("Line Segment", 400,400)
    win.setCoords(-10,-10,10,10)


    message=Text(Point(0,8),"Click for the first point").draw(win)
    p1=win.getMouse()
    p1.draw(win)
    x1=p1.getX()
    y1=p1.getY()

    message.setText("Click for the second point")
    p2=win.getMouse()
    p2.draw(win)

    
    
    x2=p2.getX()
    y2=p2.getY()

    line=Line(Point(x1,y1), Point(x2,y2)).draw(win)
              
    dx=x2-x1
    dy=y2-y1
    slope=dy/dx

    midpointX=((x1+x2)/2)
    midpointY=((y1+y2)/2)
    #p3=Point(midpointX, midpointY).draw(win)
    #p3.setFill("cyan")
    circle=Circle(Point(midpointX,midpointY), 0.15).draw(win)
    circle.setFill("cyan")
    length=sqrt((dx**2)+(dy**2))
    
    message.setText("The length of the line is: "+str(round(length,2)))
    messageSlope=Text(Point(0,7),"The slope of the line is: "+str(round(slope, 2))).draw(win)
    messageX=Text(Point(0,6),"The Midpoint of the line is: ("+str(round(midpointX ,2))).draw(win)
    messageY=Text(Point(7,6),","+str(round(midpointY, 2))).draw(win)
    messageLastParanthesis=Text(Point(8,6),")").draw(win)
    messageClose=Text(Point(0,5),"Click to close the window").draw(win)
    
    win.getMouse()
    win.close()
    
main()
