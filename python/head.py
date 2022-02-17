from graphics import*
def main():
    win=GraphWin("Face", 400,400)
    win.setCoords(-10,-10,10,10)
    head= Circle(Point(0,0), 10).draw(win)
    leftEye=Circle(Point(-7,4),1.5).draw(win)

    rightEye=leftEye.clone()
    rightEye.move(10,0)
    rightEye.draw(win)
main()



