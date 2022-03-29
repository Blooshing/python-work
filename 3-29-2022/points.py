from math import *
from graphics import*

def square(x):
    return x*x

def distance(p1, p2):

    dist = sqrt(square(p1.getX()-p2.getX()))+square(p1.getY()-p2.getY())

    return dist

def main():
    win = GraphWin("Points", 400, 400)
    point1 = win.getMouse().draw(win)
    point2 = win.getMouse().draw(win)

    print("The distance between the points is:", distance(point1,point2))
    
main()
