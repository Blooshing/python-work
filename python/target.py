from graphics import*
def main():
    win=GraphWin("Archery Target", 400,400)
    win.setCoords(-10,-10,10,10)
    white=Circle(Point(0,0), 5)
    white.setFill("White")
    white.draw(win)
    
    black=Circle(Point(0,0), 4)
    black.setFill("black")
    black.draw(win)

    blue=Circle(Point(0,0), 3)
    blue.setFill("blue")
    blue.draw(win)

    red=Circle(Point(0,0), 2)
    red.setFill("red")
    red.draw(win)

    yellow=Circle(Point(0,0), 1)
    yellow.setFill("yellow")
    yellow.draw(win)
main()
