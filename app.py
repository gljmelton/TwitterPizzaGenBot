#main app

import tweepy, time, toppings, beverages, random

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

for i in range(4):
    top1 = random.choice(toppings.top)
    top2 = random.choice(toppings.top)
    bev = random.choice(beverages.bev)
    print(("A " + top1.name + " and " + top2.name + " pizza with a 2 liter of " + bev.name))
    time.sleep(1)

def GenerateAPizza():
#figure out how many toppings
#determine crust
#how many of these pizzas to order

    return "This is the pizza"
