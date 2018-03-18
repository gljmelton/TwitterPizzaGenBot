#toppings
class topping(object):
    name = ""
    probability = 100

    def __init__(self, name, prob):
        self.name = name
        self.probability = prob

top = [topping("pepperoni", 50),
        topping("black olive", 50),
        topping("lego", 5),
        topping("caviar", 12),
        topping("green olive", 40),
        topping("pineapple", 35),
        topping("bacon", 40),
        topping("ham", 40),
        topping("banana pepper", 45),
        topping("green pepper", 45),
        topping("jalapeno", 35),
        topping("sausage", 50),
        topping("bionicle", 3),
        topping("Nintendo Switch cartridge", 3),
        topping("slices of bread", 4),
        topping("bagel bite", 8),
        topping("another, smaller pizza", 4),
        topping("mushroom", 45)]
