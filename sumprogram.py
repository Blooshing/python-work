#program.py
#Mitchell McCulley
#02/08/2022

def main():
    n = eval(input("How many values do you want to add?:"))
    sum = 0
    for i in range(n):
        num=eval(input("Enter a value to add it:"))
        sum = sum+num
        
    print("The total is:", sum)

main()

