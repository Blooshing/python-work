from math import*

def main():
    a= eval(input("please enter the first coefficient: "))
    b = eval(input("please enter the second coefficient: "))
    c = eval(input("please enter the third constant: "))

    disc = b**2-4*a*c

    if disc > 0:
         root1=(-b+sqrt(disc))/(2*a)
         root2=(-b-sqrt(disc))/(2*a)

         print("The roots are:", root1, "and", root2)

    elif disc==0:
            print("The equation has two identical roots", (-b/(2*a)))

    else:
        print("The equation has no real roots")
main()
