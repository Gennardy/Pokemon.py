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

def ask_user_choose():
    pokemon_list = [
        Bulbasaur(),
        Charmander(),
        Squirtle(),
    ]
    chose_pokemon_prompt = """1. Bulbasaur\n2. Charmender\n3. Squirtle\nPlease choose your pokemon (1/2/3):"""
    user_choice = int(input(chose_pokemon_prompt))
    return pokemon_list[user_choice-1]



computer = select_random_pokemon()
user = ask_user_choose()
print(computer)
print(user)


