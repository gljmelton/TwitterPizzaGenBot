class crust(object):
    name=""
    probability=0

    def __init__(self,name,probability):
        self.name = name
        self.probability = probability

crusts = ["thicc crust",
            "thin crust",
            "deep dish",
            "pan crust",
            "stuffed crust",
            "waffle crust",
            "sicilian crust",
            "flatbread",
            "bagel crust"]

sizes = ["personal",
            "small",
            "medium",
            "large",
            "very large"]

def GetCrust():
    return random.choice(crusts)

def GetSize():
    return random.choice(sizes)
