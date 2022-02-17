from graphics import*

def main():
    win=GraphWin("GUI moment", 300, 200)
    
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    Text(Point(1,3), "Celsius Temperature:").draw(win)
    
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    
    input=Entry(Point(2,3), 5)
    
    input.setText("0.0")
    
    input.draw(win)
    
    output=Text(Point(2,1),"").draw(win)
    
    button=Text(Point(1.5, 2.0), "Convert")
    
    button.draw(win)
    
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    
    win.getMouse()
    
    celsius=eval(input.getText())
    
    t = 9.0/5.0 * celsius +32
    
    output.setText(t)
    
    button.setText("Quit")
    
    win.getMouse()
    
    win.close()
    
main()
    
