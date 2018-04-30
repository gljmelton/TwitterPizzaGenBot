#toppings

import random

class topping(object):
    name = ""
    probability = 100

    def __init__(self, name, prob):
        self.name = name
        self.probability = prob


def GetTopping():
    return random.choice(top)

def GetValidTopping(excludeToppings = []):
    tempTopping = GetTopping()
    while True:
        if tempTopping in excludeToppings:
            tempTopping = GetTopping()
        else: break
    return tempTopping

top = [ "pepperoni",
        "black olives",
        "legos",
        "caviar",
        "green olives",
        "pineapple",
        "bacon",
        "ham",
        "banana peppers",
        "green peppers",
        "jalapenos",
        "sausage",
        "Bionicles",
        "Nintendo Switch cartridges",
        "slices of bread",
        "bagel bite",
        "smaller pizzas",
        "mushrooms",
        "onion",
        "pulled pork",
        "chorizo",
        "elotes",
        "lasagna",
        "spaghetti",
        "pasketi",
        "jelly beans",
        "blue jeans",
        "candid photos of Nicolas Cage",
        "a VHS copy of The Never Ending Story",
        "crayons",
        "a handfull of dice",
        "mandarin oranges",
        "green beans",
        "the bullet that killed Biggie",
        "corn",
        "a big stinky bean",
        "espresso beans"]
