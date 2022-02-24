from graphics import*


def main():
    win=GraphWin("Rectangle", 400,400)
    win.setCoords(0,0,10,10)
    message=Text(Point(4.5,9), "Click on the lower left corner of the rectangle")
    message.draw(win)

    p1=win.getMouse()
    message.setText("Click on the upper right corner of the rectangle")

    p2=win.getMouse()

    rectangle=Rectangle(p1,p2).draw(win)
    x1=p1.getX()
    y1=p1.getY()
    x2=p2.getX()
    y2=p2.getY()
    width =abs(x2-x1)
    length= abs(y2-y1)
    area=length*width
    perimeter=2*(length+width)

    print("The area is:", area, "the perimeter is:", perimeter,)

    message1=Text(Point(4.5,2),"The area is: "+str(round(area)))
    message1.draw(win)

    message2=Text(Point(4.5,1),"The perimeter is: "+str(round(perimeter)))
    message2.draw(win)

    message.setText("Click to closer the window")
    win.getMouse()
    win.close()
    
main()
    
