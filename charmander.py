class Charmander:
    def __init__(self):
        self.name = "Charmander"
        self.type = "Fire"
        self.attack = 20
        self.hp = 100
        self.move1 = "Ember"
        self.move2 = "Quick Attack"
        self.move3 = "Protect"
        self.move4 = "Thunder Punch"
    def assign_enemy(self,enemy):
        self.enemy = enemy

    def move1(self):
        if self.enemy.type == "Grass":
            self.enemy.hp -= (self.attack * 2)
        elif self.enemy.type == "Water":
            self.enemy.hp -= (self.attack * 0.5)
        else:
            self.enemy.hp -= self.attack
        print(f"{self.name} use {self.move1}")

    def move2(self):
        self.enemy.hp -= self.attack
        print(f"{self.name} use {self.move2}")

    def move3(self):
        self.hp += self.enemy.attack
        print(f"{self.name} use {self.move3}")

    def move4(self):
        if self.enemy.type == "Grass":
            self.enemy.hp -= (self.attack * 0.5)
        elif self.enemy.type == "Water":
            self.enemy.hp -= (self.attack * 2)
        else:
            self.enemy.hp -= self.attack
        print(f"{self.name} use {self.move4}")