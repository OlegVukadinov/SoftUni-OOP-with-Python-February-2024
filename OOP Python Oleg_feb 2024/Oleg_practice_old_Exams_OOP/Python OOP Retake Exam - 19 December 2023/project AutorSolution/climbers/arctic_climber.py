from project import BaseClimber
from project import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH = 200
    MINIMUM_STRENGTH_TO_CLIMB = 100

    def __init__(self, name: str):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        difficulty_multiplier = 2.0 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20.0 * difficulty_multiplier
        self.conquered_peaks.append(peak.name)