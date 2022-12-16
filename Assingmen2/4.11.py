pizza_abuzar=['Chicago Pizza','Siclian Pizza','Greek Pizza','Deep 
Disha Pizza']
# Copying List to an other List
friend_pizza_abuzar=pizza_abuzar[:]
#Inserting new item in original List
pizza_abuzar.append('Fajeeta')
#inserting mew item to firends Pizza list
friend_pizza_abuzar.append('BoneFire')
print("My Favorite pizzas are:")
for pizzas in pizza_abuzar:
 print(pizzas)
 
print("\nMy friend's Favorite pizzas are:")
for friend_pizzas in friend_pizza_abuzar:
 print(friend_pizzas)
My Favorite pizzas are:
Chicago Pizza
Siclian Pizza
Greek Pizza
Deep Disha Pizza
Fajeeta
My friend's Favorite pizzas are:
Chicago Pizza
Siclian pizza
Greek Pizza
Deep Disha Pizza
BoneFire
