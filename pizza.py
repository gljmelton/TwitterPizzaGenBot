class Pizza(object):
    size = ""
    toppings = []
    quantity = 0
    crust = ""

    def __init__(self, size, topping, quantity, crust):
        self.size = size
        self.toppings = topping
        self.quantity = quantity
        self.crust = crust

    def PizzaString(self):
        result = ""
        result += str(self.quantity) + "x " + self.size + " " + self.crust
        for i in self.toppings:
            result += " " + i
        result += " pizza"
        return result
