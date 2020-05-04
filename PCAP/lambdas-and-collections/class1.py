class vehicle():
    default_tire = "tire"

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    def description(self):
        return f"A vehicle with an {self.engine} engine, and {self.tires} tires"

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = (cls.default_tire, cls.default_tire)
    #     return cls(None, tires)

class bikeclass(vehicle):
    def __init__(self, tires=None):
        if not tires:
            tires = (self.default_tire, self.default_tire)
        self.tires = tires
    

# bike = vehicle.bicycle("Front and Rear")
# print(bike.tires)
car = vehicle("diesel",4)
# description = car.description()
print(car.engine)
print(car.description())

# bike2 = bikeclass(['front','rear'])
# print(bike2.tires)
# print(bike2.description)