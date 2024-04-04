class LowFuelError(Exception):
    pass

class NotEnoughError(Exception):
    pass

class Car:
    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight=weight
        self.started=started
        self.fuel=fuel
        self.fuel_consumption=fuel_consumption

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started=True
            else:
                raise LowFuelError("Нет топлива")
        return self.started

    def move(self, distance):
        self.distance = distance
        fuel_for_distance = self.distance * self.fuel_consumption
        if self.fuel >= fuel_for_distance:
            self.fuel = self.fuel - fuel_for_distance
        else:
            raise NotEnoughError("Недостаточно топлива")
        return self.fuel

BMW = Car(1640, 50,5,False)
BMW.start()
BMW.move(5)
BMW.move(15)