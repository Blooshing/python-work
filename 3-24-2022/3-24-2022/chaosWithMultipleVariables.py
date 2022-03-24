def chaos():
    x1 = eval(input("Enter a number from 0 to 1: "))
    x2 = eval(input("Enter a value between 0 and 1: "))

    index = eval(input("Enter the number of interations: "))
    print("{0}\t\t{1}{2:>25}".format("Index", "X1", "X2"))
        
    for i in range (index+1):
        x1 = 3.9*x1*(1-x1)
        x2 = 3.9*x2*(1-x2)
        print("{0}\t\t{1:0.7f}{2:>25.7f}".format(i,x1,x2))
chaos()
