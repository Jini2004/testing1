class Character:
    def __init__(self, name, health):
        self.name = name 
        self.health = health
        
    def attack(self):
        print(f"{self.health}")

class Player(Character):
    def __init__(self, name, level, health):
        super(). __init__(name, health) #we using super bcz to we dont wanna repeat the same stuff in base class
        #self.name = name 
        self.level = level
        #self.health = health

    def attack(self):
        print(f"{self.name} Attck the enemey")

    def heal(self, amount):
        self.health += amount
        print(f"{self.health} Heal")


class Enemy(Character):
    def __init__(self, name, level, health, attacktype):
        super(). __init__(name, health)
        #self.name = name
        self.level = level
        #self.health = health
        self.attacktype = attacktype

    def attack(self):
        print(f"{self.name} Attack")

    def heal(self, amount):
        self.health += amount        
        print(f"{self.health} Heal")

    def defend(self):
        print(f"{self.name} Defend")    

#Player1 = Player("Hero", 10, 100)
#Enemy1 = Enemy("Gobline", 9, 85, "Ice")
#Enemy2 = Enemy("Dragon", 10, 95, "Fire")

Player1 = Player("Rajini", 10, 100)
Enemy1 = Enemy("Hasan", 9, 85, "Ice")
Enemy2 = Enemy("Toan", 10, 95, "Fire")


Player1.attack()
Enemy1.attack()
Enemy2.attack()

Player1.heal(35)

Enemy1.defend()