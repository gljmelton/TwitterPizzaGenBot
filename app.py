#main app

#2x Large Thin-crust Pepperoni and Lasagna Pizza
#1x Sixer of Pepsi
#

import tweepy, time, toppings, beverages, crust, pizza, random, sys, local_settings



auth = tweepy.OAuthHandler(local_settings.CONSUMER_KEY, local_settings.CONSUMER_SECRET)
auth.set_access_token(local_settings.ACCESS_TOKEN, local_settings.ACCESS_SECRET)

api = tweepy.API(auth)

#for each pizza ordered, determine the amount of that pizza to order
def DetermineOrderQuantity():
    return random.randint(1,99)

#how many different pizzas to order
def DeterminePizzaAmount():
    return random.randint(1,4)

def BuildAPizza():
    pizzAmount = DeterminePizzaAmount()
    pickedToppings = []
    for i in range(0, pizzAmount):
        pickedToppings.append(toppings.GetValidTopping(pickedToppings))

    pizzaOrder = pizza.Pizza(random.choice(crust.sizes), pickedToppings, DetermineOrderQuantity(), random.choice(crust.crusts))
    return pizzaOrder


finalPizza = BuildAPizza()

#A large thin crust pineapple & ham pizza
finalOrder = "A " + finalPizza.size + " " + finalPizza.crust + " pizza topped with "

for x in range(0, len(finalPizza.toppings)):
    finalOrder += finalPizza.toppings[x] + " "
    if x < (len(finalPizza.toppings)-1):
        finalOrder += "& "

print(finalOrder)
raw_input('Press Enter to exit')

    #determine beverage

    #concatenate into tweet
