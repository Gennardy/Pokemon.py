from bulbasaur import Bulbasaur 
from charmander import Charmander 
from squirtle import Squirtle 
import random


def select_random_pokemon():
    pokemon_list = [
        Bulbasaur(),
        Charmander(),
        Squirtle(),
    ]
    return random.choice(pokemon_list)



computer = select_random_pokemon()

print(computer)


