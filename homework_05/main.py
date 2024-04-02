class VehicleBase:
    def __init__(self, weight):
        self.weight=weight

weight_of_transport = VehicleBase (680)
print(weight_of_transport)

class Ship(VehicleBase):
    def __init__(self, weight, max_weight):
        super().__init__(weight)
        self.max_weight =max_weight

    def set_sail (self):
        print("Поднять паруса!!!")

    def __str__(self):
        return (
            f"Weight:{self.weight} "
            f"Max_weight:{self.max_weight} "
        )

# Saint_Petr = Ship(200000, 360000)
# Saint_Petr.set_sail()
# print(Saint_Petr)
class Plan(VehicleBase):
    def __init__(self, weight, cargo=0):
        super().__init__(weight)
        self.cargo = cargo

    def add_cargo(self, cargo):
        self.cargo+=cargo
       # return self.cargo

    def __str__(self):
        return (
            f"Weight:{self.weight} "
            f"Cargo:{self.cargo} "
        )

# butterfly = Plan(150000)
# print(butterfly)
# butterfly.add_cargo(3)
# print(butterfly)
# butterfly.add_cargo(5)
# print(butterfly)

def main():
    Saint_Petr = Ship(200000, 360000)
    print(Saint_Petr)
    Saint_Petr.set_sail()
    butterfly = Plan(150000)
    print(butterfly)
    butterfly.add_cargo(3)
    print(butterfly)
    butterfly.add_cargo(5)
    print(butterfly)

if __name__=="__main__":
    main()