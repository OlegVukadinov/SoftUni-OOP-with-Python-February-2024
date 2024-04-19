from project.band_members.musician import Musician

AVAILABLE_SKILLS_TO_LEARN = ("sing high pitch notes", "sing low pitch notes")


class Singer(Musician):

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.available_skills_to_learn = AVAILABLE_SKILLS_TO_LEARN



