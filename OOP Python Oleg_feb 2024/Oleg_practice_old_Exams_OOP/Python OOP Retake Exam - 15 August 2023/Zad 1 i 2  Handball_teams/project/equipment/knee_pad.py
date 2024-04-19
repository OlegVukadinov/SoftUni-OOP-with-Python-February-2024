from project import BaseEquipment


class KneePad(BaseEquipment):

    def __init__(self):
        super().__init__(120, 15.0)

    def increase_price(self):
        self.price *= 1.2
