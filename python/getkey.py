#getKey
from graphics import*
def main():
    win=GraphWin("Interactive", 500, 500)
    win.setCoords(0,0,10,10)
    for i in range(8):
        p=win.getMouse()
        key=win.getKey()
        Text(p,key).draw(win)
main()
