#main app

import tweepy, time, toppings, beverages, random

CONSUMER_KEY = 'Ou0smfZnSunVSG5HT37vxNSRf'
CONSUMER_SECRET = 'Q2BfUk5f97B7w5ziIVi27aTAvDYP1t41AhZRQRgK2Ls4uSGFyH'
ACCESS_TOKEN = '974709958381010945-EUSAcQYJFgExpiZEVHnMApXrgAvM6Z8'
ACCESS_SECRET = 'J9C1Q5Y8X5hoAOfejl6hwbKHKrT30NdjtIDpKeODTRzXA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

for i in range(4):
    top1 = random.choice(toppings.top)
    top2 = random.choice(toppings.top)

    print(("A " + top1 + " and " + top2 + " pizza with a 2 liter of " + (random.choice(beverages.bev))))
    time.sleep(1)

def GenerateAPizza():
#figure out how many toppings
#determine crust


    return "This is the pizza"

def
