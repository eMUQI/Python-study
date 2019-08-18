list_of_pizza = ["pizza1", "pizza2", "pizza3"]
friend_pizzas = list_of_pizza[:]
list_of_pizza.append("pizza4")
friend_pizzas.append("pizza5")
print("My favorite pizzas are: %s"% str(list_of_pizza))
print("My friends favorite pizzas are: %s"%str(friend_pizzas))