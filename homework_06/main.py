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
        if self.fuel >= self.distance * self.fuel_consumption:
            self.fuel = self.fuel - self.distance * self.fuel_consumption
        else:
            raise NotEnoughError("Недостаточно топлива")
        return self.fuel

BMW = Car(1640, 50,5,False)
BMW.start()
BMW.move(5)
BMW.move(15)
BMW.move(1)