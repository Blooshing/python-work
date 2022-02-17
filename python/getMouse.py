#getMouse
from graphics import*
def main():
    win=GraphWin("Mouse Clicks",400,400)
    win.setCoords(0,0,10,10)

    message=Text(Point(5,9), "Click on the first point").draw(win)
    p1= win.getMouse()

    p1.draw(win)

    message.setText("Click on the second point")

    p2=win.getMouse()
    p2.draw(win)

    message.setText("Click on the third point")
    p3=win.getMouse()
    p3.draw(win)

    triangle=Polygon(p1,p2,p3)

    triangle.draw(win)
    triangle.setFill("light green")

    triangle.setOutline("hot pink")

    message.setText("Click on the window to close it")

    win.getMouse()
    win.close()
        
    
main()
