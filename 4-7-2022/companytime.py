#company time
def main():
    rate = eval(input("Please enter your hourly rate: "))
    hours = eval (input("How many hours did you work this week?: "))

    if hours > 40:
        totalPay = (rate * 1.5) * hours
    else:
        totalPay = rate*hours
    print("You earned", totalPay,"this week.")
main()
