#generalized factorial

def genFac():
    n=eval(input("What is the number you want to calcuate the factorial of?:"))
    factor=1
    for i in range (n,1,-1):
        factor=factor*i

    print("The factor of",n,"is:", factor)
genFac()
