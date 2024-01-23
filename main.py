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
        computer.move1,
        computer.move2,
        computer.move3,
        computer.move4
    ]
    return random.choice(enemy_moveset)


computer = select_random_pokemon()
user = ask_user_choose()
print(f"You choose {user.name}")
print(f"The computer choose {computer.name}")

user.assign_enemy(computer)
computer.assign_enemy(user)

user_moveset = [user.move1, user.move2, user.move3, user.move4]
user_pp = [user.move1_pp, user.move2_pp, user.move3_pp, user.move4_pp]
while continue_game:
    print("Choose your move: ")
    print(user.move1_name)
    print(user.move2_name)
    print(user.move3_name)
    print(user.move4_name)
    user_move = int(input("Please select a move: (1,2,3,4) "))
    count_pp = user_pp[user_move-1]
    print(user_pp)
    while count_pp <= 0:
        print("Invalid choice, The PP = 0")
        print("Choose your move: ")
        print(user.move1_name)
        print(user.move2_name)
        print(user.move3_name)
        print(user.move4_name)
        user_move = int(input("Please select a move: (1,2,3,4) "))
        count_pp = user_pp[user_move - 1]
    user_moveset[user_move -1]()
    enemy_move_choose = enemy_move()
    enemy_move_choose()
    if user.hp <= 0:
        print("Your HP fall below 0, Computer Win")
        continue_game = False
    elif computer.hp <= 0:
        print("Computer's HP fall below 0, You Win")
        continue_game = False
    else:
        print(user.hp)
        print(computer.hp)