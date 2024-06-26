from project import Movie
from project import User


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

# u = User("test", 56)
# f = Thriller("asd", 1990, u, 45)
# print(f.details())
