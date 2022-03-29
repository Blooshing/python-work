def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i]*(1+rate)

        
    

def main():
    amounts = [1000,1500,2000,2500]
    rate = 0.25

    addInterest(amounts, rate)

    print("You will have", amounts)
main()
