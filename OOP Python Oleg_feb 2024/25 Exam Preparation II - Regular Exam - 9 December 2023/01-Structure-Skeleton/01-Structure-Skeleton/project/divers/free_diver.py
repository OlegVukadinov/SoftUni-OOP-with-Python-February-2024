from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        # reduce_amount = round(0.6 * time_to_catch)
        # if (self.oxygen_level - reduce_amount) < 0:
        #      self.oxygen_level = 0
        # else:
        #      self.oxygen_level -= reduce_amount

        if self.oxygen_level >= time_to_catch:
            self.oxygen_level -= round(60 * time_to_catch / 100)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.INITIAL_OXYGEN

