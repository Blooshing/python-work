def main():
    score = eval(input("Please enter your test score: "))

    if score > 90:
        print("You got an A")
    elif score > 80:
        print("Your grade is a B")
    elif score > 70:
        print("You got a C")
    elif score > 60:
        print("You got a D")
    else:
        print("You have failed the exam")
    
main()
