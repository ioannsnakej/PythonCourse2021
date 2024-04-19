from pydantic import BaseModel
from exceptions import LowFuelError

class VehicleBase(BaseModel):
    color: str

class Car(VehicleBase):
    fuel: int
    started: bool = False

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError("Нет топлива!")

    def stop(self):
        if self.started == True:
            self.started = False

class Plane(VehicleBase):
    cargo: int
    max_cargo: int

    def add_cargo(self, cargo):
        if self.cargo+cargo < self.max_cargo:
            self.cargo+=cargo
        else:
            raise ValueError("Превышен лимит груза")
    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo=0
        return old_cargo

def demo_car():
    BMW=Car(color="black",fuel=50, started=False)
    print("BMW =", BMW)
    BMW.start()
    print("Started:", BMW.started)
    BMW.stop()
    print("Started:", BMW.started)
    Toyota=Car(color="red",fuel=0)
    print("Toyota =", Toyota)
    #Toyota.start()

def demo_plane():
    Birdman = Plane(color="black", cargo=100, max_cargo=300)
    print("Birdman:", Birdman)
    Birdman.add_cargo(150)
    print("Birdman:", Birdman)
    #Birdman.add_cargo(150)
    print("Remove all cargo, old cargo=", Birdman.remove_all_cargo())
    print("Birdman:", Birdman)
    print("Birdman:", Birdman)
    Birdman.add_cargo(150)
    print("Birdman:", Birdman)
    Birdman.add_cargo(150)


def main():
    demo_car()
    demo_plane()


if __name__ == '__main__':
    main()