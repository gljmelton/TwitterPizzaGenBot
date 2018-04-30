#beverages

class beverage(object):
    name = ""
    probability = 100

    def __init__(self, name, prob):
        self.name = name
        self.probability = prob

class bevSize(object):
    name = ""
    probability = 100

    def __init__(self, name, prob):
        self.name = ""
        self.probability = 100

bev = ["pepsi",
       "coke",
       "water",
       "milk",
       "piss",
       "bug juice",
       "gatorade",
       "wine",
       "beer"
        ]

sizes = ["can",
         "sixer",
         "gallon",
         "pint",
         "keg",
         "bottle",
         "two-liter",
         "carton",
         "box",
         "big bag",
         "small bag",
         "ziploc bag",
         "condom",
         "bowl"]
