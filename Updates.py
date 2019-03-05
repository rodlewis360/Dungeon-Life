class Person:
    def __init__(self, HP, attacks, HPlimit, meleeweapon, magicweapon, healthpotions, waited):
        self.HP = HP
        self.attacks = attacks
        self.HPlimit = HPlimit
        self.meleeweapon = meleeweapon
        self.magicweapon = magicweapon
        self.healthpotions = healthpotions
    def attack(currentenemy, obj):
        import random
        print("What would you like to do(Attack, Heal, Wait, or Flee)?")
        print("You have", HP, "HP. ", currentenemy.name, "has", currentenemy.HP, "HP.")
        whattodo = input()
        if whattodo == 'Attack':
            print("What attack would you like to use", """(stick, sword, fire, or sparks[same capitalization])?""")
            attack = input()
            for a in attacks:
                if a == attack:
                    print("You use", a.name, "on", currentenemy.name, "doing", a.damage, "damage.")
                    currentenemy.HP -= a.damage
        if whattodo == 'Heal':
            if HP + 2.5 > HPlimit:
                print("You have too much health.")
            else:
                print("You drink 1 health potion.")
        if whattodo == 'Wait':
            print("You wait for", currentenemy.name, "'s attack, hoping to dodge it.")
            waited = True
        if whattodo == 'Flee':
            dice = [1, 2]
            import random
            diceroll = random.choice(dice)
            if diceroll == 1:
                print("You run away, your feet flying.")
                return True
        return False


class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Enemy:
    def __init__(self, name, attacks, HP, drops):
        self.name = name
        self.attacks = attacks
        self.HP = HP
    def attack(currentperson, obj, ran):
        import random
        dice = [1, 2]
        attack = random.choice(attacks)
        if currentperson.waited != True:
            print(name, "used", attack.name, "doing", attack.damage, "damage.")
            currentperson.HP -= attack.damage
            currentperson.waited = False
        else:
            diceroll = random.choice(dice)
            if diceroll == 1:
                print(name, "missed you while trying to do", attack.name, ".")
            else:
                print(name, "used", attack.name, "doing", attack.damage, "damage.")
                currentperson.HP -= attack.damage
            

def DungeonLife():
    player = Person(10, [ Attack('stick', 1.5), Attack('fire', 2.5)], 10, 'stick', 'fire', 5, False)
    from time import sleep
    monsterskilled = 0
    enemies = [Enemy['snake', [Attack('bite', 2.5), Attack('spit', 1)], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks']), Enemy['snake', [Attack('bite', 2.5), Attack('spit', 1)], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks']), Enemy['snake', [Attack('bite', 2.5), Attack('spit', 1)], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks']), Enemy('spider', [Attack('bite', 2.5), Attack('web', 1.5)], 2.5, ['iron armor', 'sword', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion']), Enemy('spider', [Attack('bite', 2.5), Attack('web', 1.5)], 2.5,   
        if level == 15:
            print("You find a tablet bearing this message:")
            sleep(1)
            print("\"You terrible man!  You took the lives of countless people and now you shall pay!\"")
            sleep(1)
            print("You wonder what this is all about.")
            sleep(1)
            print("You can't worry right now, though, because a monster that looks like Medusa jumps out of a corner!")
            Medusa = Enemy('Medusa', [Attack('slash', 5), Attack('bite', 2.5), Attack('smash', 7.5)], 25, ['armor of Paul Revere', 'sword of fire', 'cursed flames'])
            player.HPlimit = 20
            while player.HP > 0.1 and Medusa.HP > 0.1:
                Medusa.attack(player, player.attack(Medusa))
            if player.HP > 0.1:
                print("You vanquished Medusa!")
                drop = random.choice(Medusa.drops)
    print("You died...")
    print("You killed", monsterskilled, "monsters.")
    print("You got to level", level, ".")


DungeonLife()
