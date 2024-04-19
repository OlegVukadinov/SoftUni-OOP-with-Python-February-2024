from project import Movie
from project import User


class Action(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, " \
               f"Owned by:{self.owner.username}"

# u = User("test", 56)
# f = Action("asd", 1996, u,45)
# print(f.details())
