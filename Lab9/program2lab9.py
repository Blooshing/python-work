from graphics import*

def moveTo(shape, newCenter):
    center = shape.getCenter()

    dx = newCenter.getX() - center.getX()
    dy = newCenter.getY() - center.getY()

    shape.move(dx,dy)

def main():
    win = GraphWin("Moving Circle", 400,400)
    win.setCoords(-10,-10,10,10)

    circle = Circle(Point(0,0),0.5).draw(win)

    for i in range(10):
        p = win.getMouse()
        moveTo(circle, p)
    win.getMouse()
    win.close()
main()
