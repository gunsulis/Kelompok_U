class Hero:  # template

    def __init__(self, InputName, InputArmor, InputPower, InputHealth):
        self.name = InputName
        self.armor = InputArmor
        self.power = InputPower
        self.health = InputHealth


hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("adam", 200, 10, 30)
hero3 = Hero("mamah", 100, 20, 30)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
