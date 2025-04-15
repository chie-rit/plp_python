"""
implementation of one piece characters
using classes
"""

class Character():
    def __init__(self, name, role, group, is_active):
        self.name = name
        self.role = role
        self.group = group
        self.is_active = is_active

    def introduce(self):
        print(f'I am {self.name} and I am a {self.role}!')

    def adventure(self):
        if self.is_active and self.role == 'pirate':
            print('Going on an adventure')
        else:
            print('Too tired to go on an adventure')
        

class FruitUser(Character):
    def __init__(self, name, role, group, ability, is_active):
        super().__init__(name, role, group, is_active)
        self.ability = ability

    def adventure(self):
        print('I cannot swim')
    
    def use_ability(self):
        print(f'{self.name} is activating their ability {self.ability}')

zorro = Character("Zorro", "Swordsman", "strawhats", True)
zorro.introduce()


luffy = FruitUser("luffy", "pirate", "strawhats", "gum gum fruit", True)
luffy.introduce()
luffy.use_ability()