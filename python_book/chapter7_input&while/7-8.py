sandwich_orders = ["sandwichA", 'sandwichB', 'sandwichC']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwich.append(sandwich)
    print("i made your "+sandwich)
print("finished_sandwich:"+str(finished_sandwich))