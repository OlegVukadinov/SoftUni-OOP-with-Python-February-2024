
from typing import List
from project import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p_obj in self.pokemons:
            if p_obj.name == pokemon_name:
                self.pokemons.remove(p_obj)
                return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    # Option -> fast and short
    # try:
    #     pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
    # except StopIteration:
    #     return "Pokemon is not caught"

    def trainer_data(self):
        info = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            info.append(f"- {p.pokemon_details()}")
        return "\n".join(info)

  # Option
        # pokemons_data = '\n'.join(f"- {p.pokemon_details()}" for p in self.pokemons)
        # return f"Pokemon Trainer {self.name}\n" \
        #        f"Pokemon count {len(self.pokemons)}\n" \
        #        f"{pokemons_data}"

# Test Code
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

