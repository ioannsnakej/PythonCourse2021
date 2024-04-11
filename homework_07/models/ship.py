from .vehicle_base import VehicleBase
class Ship(VehicleBase):
    def __init__(self, weight, max_weight):
        super().__init__(weight)
        self.max_weight =max_weight

    def set_sail(self):
        print("Поднять паруса!!!")

    def __str__(self):
        return (
            f"Weight:{self.weight} "
            f"Max_weight:{self.max_weight} "
        )