class Hero:  # template
    # class variable
    jumlah = 0

    def __init__(self, InputName, InputArmor, InputPower, InputHealth):
        # instance variable
        self.name = InputName
        self.armor = InputArmor
        self.power = InputPower
        self.health = InputHealth
        Hero.jumlah += 1
        print("Membuat Hero dengan nama " + InputName)


hero1 = Hero("sniper", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("adam", 200, 10, 30)
print(Hero.jumlah)
hero3 = Hero("mamah", 100, 20, 30)
print(Hero.jumlah)
