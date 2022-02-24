#house
from graphics import*

win=GraphWin("House", 500, 500)
win.setCoords(0,0,10,10)

#drawing frame of the house

message=Text(Point(4.5,9), "Click on the opposite corners of the house").draw(win)

houseLL=win.getMouse()
houseUR=win.getMouse()

house=Rectangle(houseLL,houseUR).draw(win)
xLL=houseLL.getX()
xUR=houseUR.getY()
houseWidth=xUR-xLL

#drawing the door

message.setText("Click on the center of the op of the door")

doorCenter=win.getMouse()
doorWidth=0.2*houseWidth

doorUL=doorCenter.clone()
doorUL.move(-0.5*doorWidth, 0)
doorLLX=doorUL.getX()
doorLLY=houseLL.getY()

doorLL=Point(doorLLX, doorLLY)
doorUR=doorCenter.clone()
doorUR.move(0.5*doorWidth, 0)

door=Rectangle(doorLL, doorUR).draw(win)

#drawing the window
message.setText("Click on the center on the window")
windowCenter=win.getMouse()
windowWidth=doorWidth*0.5

windowUR=windowCenter.clone()
windowUR.move(0.5*windowWidth, 0.5*windowWidth)
windowLL=windowCenter.clone()
windowLL.move(-0.5*windowWidth, -0.5*windowWidth)

#drawing the roof

message.setText("Click on the peak of the roof")

peak=win.getMouse()
houseUL=houseUR.clone()
houseUL.move(-houseWidth,0)
roof = Polygon(peak, houseUR, houseUL).draw(win)
main()


