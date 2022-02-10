#cost of order

def orderCost():
    pounds=eval(input("How many pounds of coffee did you order?:"))
    cost=((pounds*10.5)+((pounds*0.86)+1.50))
    print("The cost is:",cost)

orderCost()
    
def correctOrderCost():
    weight=eval(input("How many pounds did you buy?:"))
    cost=weight*10.5
    shipping=weight*0.86+1.5
    total_cost=cost+shipping
    print("The total cost is$",total_cost)
correctOrderCost()
