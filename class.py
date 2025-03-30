class Vehicle:
    field = "Darat"
    def __init__(self, type, wheels):
        self.type = type
        self.wheels = wheels


honda = Vehicle("motor", 2)
print(honda.field + honda.type)

Vehicle.field = "Laut"
print(honda.field + honda.type)
