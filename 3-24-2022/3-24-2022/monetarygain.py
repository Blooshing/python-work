def monetaryOutput():
    investment = eval(input("Please specify an amount to deposit: "))
    interest = eval(input("What is the annual interest rate?: "))
    years = eval(input("How many years will this money accrue?: "))

    print("{0}\t\t{1}".format("Years", "Amount"))
    print("------------------------")
    print("{0}\t\t${1:0.2f}".format(0, investment))

    for i in range (1, years+1):
        investment = investment*(1+interest)

        print("{0}\t\t${1:0.2f}".format(i, investment))
monetaryOutput()
