from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        # reduce_amount = round(0.3 * time_to_catch)
        # if (self.oxygen_level - reduce_amount) < 0:
        #      self.oxygen_level = 0
        # else:
        #      self.oxygen_level -= reduce_amount

        if self.oxygen_level >= time_to_catch:
            self.oxygen_level -= round(30 * time_to_catch / 100)
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN
