from models.car import Car
from models.ship import Ship

def demo_cer():
    BMW = Car(1640, 50, 5, False)
    print(BMW.fuel)
    BMW.start()
    BMW.move(5)
    BMW.move(15)

def demo_ship():
    Saint_Petr = Ship(200000, 360000)
    print(Saint_Petr)
    Saint_Petr.set_sail()
def main():
    demo_cer()
    demo_ship()

if __name__ == '__main__':
    main()