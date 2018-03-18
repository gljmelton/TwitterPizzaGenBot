#beverages

class beverage(object):
    name = ""
    probability = 100

    def __init__(name, prob):
        self.name = name
        self.probability = prob

class bevSize(object):
    name = ""
    probability = 100

    def __init__(name, prob):
        self.name = ""
        self.probability = 100

bev = [beverage("pepsi", 50),
        beverage("coke", 50),
        beverage("water", 50),
        beverage("milk", 50),
        beverage("piss", 50),
        beverage("bug juice", 50),
        beverage("gatorade", 50),
        beverage("wine", 50),
        beverage("beer", 50)]

sizes = [bevSize("can", 50),
         bevSize("sixer", 50),
         bevSize("gallon", 50),
         bevSize("pint", 50),
         bevSize("keg", 50),
         bevSize("bottle", 50),
         bevSize("two-liter", 50),
         bevSize("carton", 50),
         bevSize("box", 50),
         bevSize("big bag", 50),
         bevSize("small bag", 50),
         bevSize("ziploc bag", 50),
         bevSize("condom", 50),
         bevSize("bowl", 50)]
