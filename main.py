from bulbasaur import Bulbasaur
from charmander import Charmander
from squirtle import Squirtle
import random

continue_game = True
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

def enemy_move():
    enemy_moveset = [
        computer.move1(),
        computer.move2(),
        computer.move3(),
        computer.move4()
    ]
    return random.choice(enemy_moveset)


computer = select_random_pokemon()
user = ask_user_choose()
print(computer)
print(user)

user_moveset = [user.move1(), user.move2(), user.move3(), user.move4()]

while continue_game:
    print(user_moveset)
    user_move = input("Please select a move: (1,2,3,4) ")
    computer_move = enemy_move()
    if user.hp() < 0 or computer.hp() < 0:
        continue_game = False
