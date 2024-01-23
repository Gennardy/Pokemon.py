class Charmander:
    def __init__(self):
        self.name = "Charmander"
        self.type = "Fire"
        self.attack = 20
        self.hp = 100
        self.move1_name = "Ember"
        self.move2_name = "Quick Attack"
        self.move3_name = "Protect"
        self.move4_name = "Thunder Punch"
        self.move1_pp = 3
        self.move2_pp = 3
        self.move3_pp = 2
        self.move4_pp = 4

    def assign_enemy(self,enemy):
        self.enemy = enemy

    def move1(self):
        self.move1_pp -= 1
        if self.move1_pp >= 0:
            if self.enemy.type == "Grass":
                self.enemy.hp -= (self.attack * 2)
            elif self.enemy.type == "Water":
                self.enemy.hp -= (self.attack * 0.5)
            elif self.enemy.type == "Fire":
                self.enemy.hp -= (self.attack * 0.5)
            else:
                self.enemy.hp -= self.attack
            print(f"{self.name} use {self.move1_name}")


    def move2(self):
        self.move1_pp -= 1
        if self.move1_pp >= 0:
            self.enemy.hp -= self.attack
            print(f"{self.name} use {self.move2_name}")

    def move3(self):
        self.hp += self.enemy.attack
        print(f"{self.name} use {self.move3_name}")

    def move4(self):
        if self.enemy.type == "Grass":
            self.enemy.hp -= (self.attack * 0.5)
        elif self.enemy.type == "Water":
            self.enemy.hp -= (self.attack * 2)
        else:
            self.enemy.hp -= self.attack
        print(f"{self.name} use {self.move4_name}")