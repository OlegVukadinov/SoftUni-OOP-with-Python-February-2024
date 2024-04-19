from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        try:
            musician = [m for m in self.musicians if m.name == name][0]
            raise Exception(f"{name} is already a musician!")
        except IndexError:
            new_musician = self.VALID_MUSICIAN_TYPES[musician_type](name)
            self.musicians.append(new_musician)
            return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        try:
            band = [b for b in self.bands if b.name == name][0]
            raise Exception(f"{name} band is already created!")

        except IndexError:
            b = Band(name)
            self.bands.append(b)
            return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        try:
            concert = [c for c in self.concerts if c.place == place][0]
            raise Exception("{place} is already registered for {genre} concert!")

        except IndexError:
            c = Concert(genre, audience, ticket_price, expenses, place)
            self.concerts.append(c)
            return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in self.musicians:
            raise Exception(f"{musician_name} isn't a musician!")
        try:
            band = [b for b in self.bands if b.name == band_name][0]
            raise Exception(f"{band_name} isn't a band!")
        except IndexError:
            existing_musician = [m for m in self.musicians if m.name == musician_name][0]
            existing_band = [b for b in self.bands if b.name == band_name][0]
            existing_band.members.append(existing_musician)
            return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in self.bands:
            raise Exception(f"{band_name} isn't a band!")

        existing_band = [b for b in self.bands if b.name == band_name][0]
        musician = [m for m in existing_band.members if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        musician = musician[0]
        existing_band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        musician_types = set([m.__class__.__name__ for m in band.members])
        if len(musician_types) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            pass

        elif concert.genre == "Metal":
            pass

        elif concert.genre == "Jazz":
            pass

