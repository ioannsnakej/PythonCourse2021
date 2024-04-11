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
        if not self.started:
            if self.fuel > 0:
                self.started=True
            else:
                raise LowFuelError("Нет топлива")
        else:
            print("Двигатель запущен")
        return self.started

    def move(self, distance):
        try:
            self.distance = distance
            if self.fuel >= self.distance * self.fuel_consumption:
                self.fuel = self.fuel - self.distance * self.fuel_consumption
            else:
                raise NotEnoughError("Недостаточно топлива")
        except NotEnoughError:
            print("Не хватает топлива, чтобы проехать:", self.distance, "км",
                  "В баке осталось:", self.fuel, "л",
                  "Не хватает еще:", self.distance * self.fuel_consumption - self.fuel, "л")

BMW = Car(1640, 50,5,False)
print(BMW.fuel)
BMW.start()
BMW.move(5)
BMW.move(15)
