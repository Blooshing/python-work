#newfile
from graphics import*
def main():
    win = GraphWin("investment Growth Chart", 320, 240)
    win.setBackground("white")

    Text(Point(20, 230), "0.0k").draw(win)
    Text(Point(20, 180), "2.5k").draw(win)
    Text(Point(20, 130), "5.0k").draw(win)
    Text(Point(20, 80), "7.5k").draw(win)
    Text(Point(20, 30), "10.0k").draw(win)

    principal=eval(input("Please enter the principal amount: "))
    apr=eval(input("Please enter the annual percentage rate: "))

    height = principal*0.02
    bar=Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("light green")
    bar.setWidth(1)
    bar.draw(win)

    for year in range(1,11):
        # calculate value fo the next year
        principal= principal*(1+apr)
        #draw bar for this value
        x11= year * 75+40
        height+principal *0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("light green")
        bar.setWidth(1)
        bar.draw(win)
main()
