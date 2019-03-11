# Only ever going to be used for a player.
class Person:
    # initiate
    def __init__(self, HP, attacks, HPlimit, healthpotions, waited, effect):
        self.HP = HP
        self.attacks = attacks
        self.HPlimit = HPlimit
        self.healthpotions = healthpotions
        self.waited = waited
        self.effect = effect
    # this is the attack section
    def attack(currentenemy, obj):
        # check for effects
        if effect == 'fire':
            HP -= 1
        if effect == 'poison':
            HP -= 0.5
        if effect == 'cursed fire':
            HP -= 1.5
        if effect == 'electricity':
            HP -= 2
            currentenemy.HP -= 0.5
            effect = 'None'
        if effect == 'heal':
            currentenemy.HP += 0.5
            effect = 'None'
        import random
        # Ask for what to do?
        print("What would you like to do(Attack, Heal, Wait, or Flee)?")
        print("You have", HP, "HP. ", currentenemy.name, "has", currentenemy.HP, "HP.")
        whattodo = input()
        # Attack process
        if whattodo == 'Attack':
            print("What attack would you like to use?")
            # print out available attacks
            for a in attacks:
                print(a.name)
            attack = input()
            # deal damage
            for a in attacks:
                if a == attack:
                    print("You use", a.name, "on", currentenemy.name, "doing", a.damage, "damage.")
                    currentenemy.HP -= a.damage
                    currentenemy.effect = a.effect
        # Healing section
        if whattodo == 'Heal':
            if HP + 2.5 > HPlimit:
                print("You have too much health.")
            else:
                print("You drink 1 health potion.")
                HP += 2.5
        if whattodo == 'Wait':
            print("You wait for", currentenemy.name, "'s attack, hoping to dodge it.")
            waited = True
        if whattodo == 'Flee':
            dice = [1, 2]
            import random
            diceroll = random.choice(dice)
            if diceroll == 1:
                print("You run away, your feet flying.")
                # variable "run"
                return True
        return False
    def between(level):
        print("What would you like to do while you're safe?")
        whattodo = input()
        if whattodo == 'show':
            # show stuff
            print("HP:", HP)
            print("HP limit:", HPlimit)
            print("attacks:")
            for a in attacks:
                print(a)
        if whattodo == 'heal':
            print("How many potions would you like to drink?")
            try:
                drink = int(input())
                if drink > healthpotions:
                    drink = healthpotions
                HP += drink * 2.5
            except ValueError or TypeError:
                if drink == 'l3v3l':
                    level = int(input()) - 1
                    return level

# Attack class
class Attack:
    def __init__(self, name, damage, effect):
        self.name = name
        self.damage = damage
        self.effect = effect

# enemies
class Enemy:
    def __init__(self, name, attacks, HP, drops, effect):
        self.name = name
        self.attacks = attacks
        self.HP = HP
        self.drops = drops
        self.effect = effect
    def attack(currentperson, obj, ran):
        # check for effects and deal damage accordingly
        if effect == 'poison':
            HP -= 0.5
        if effect == 'fire':
            HP -= 1
        if effect == 'cursed fire':
            HP -= 1.5
        if effect == 'electricity':
            HP -= 2
            currentperson.HP -= 0.5
            effect = 'None'
        if effect == 'heal':
            currentperson.HP += 0.5
            effect = 'None'
        # attack the player
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
                currentperson.effect = attack.effect
    def drop(currentperson, obj):
        drop = random.choice(drops)
        # drop effects
        if drop == 'iron armor':
            currentperson.HPlimit = 15
        if drop == 'steel armor':
            currentperson.HPlimit = 20
        if drop == 'orc armor':
            currentperson.HPlimit = 30
        if drop == 'armor of Paul Revere':
            currentperson.HPlimit = 40
        if drop == 'sword':
            currentperson.attacks.append(Attack('sword', 3.5, 'None'))
        if drop == 'poison fang':
            currentperson.attacks.append(Attack('poison fang', 5), 'poison')
        if drop == 'sparks':
            currentperson.attacks.append(Attack('sparks', 3, 'electricity'))
        if drop == 'cursed flames':
            currentperson.attacks.append(Attack('cursed flames', 7.5, 'cursed fire'))
        if drop == 'healthpotion':
            currentperson.healthpotions += 1
        print(name, "dropped", drop, ".")
            

def DungeonLife():
    player = Person(10, [ Attack('stick', 1.5, 'None'), Attack('fire', 2.5, 'fire')], 10, 5, False, None)
    from time import sleep
    monsterskilled = 0
    # define 'snake' and 'spider'
    snake = Enemy('snake', [Attack('bite', 2.5, 'poison'), Attack('spit', 1, 'None')], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks'], None)
    spider = Enemy('spider', [Attack('bite', 2.5), Attack('web', 1.5)], 2.5, ['iron armor', 'sword', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion'], None)
    # Start game
    enemies = [snake, snake, snake, spider, spider]
    while player.HP > 0.1:
        level = player.between(level)
        enemy = random.choice(enemies)
        enemy.attack(player, player.attack)
        # drop system
        enemy.drop(player)
        # Medusa boss battle
        if level == 15:
            print("You find a tablet bearing this message:")
            sleep(1)
            print("\"You terrible man!  You took the lives of countless people and now you shall pay!\"")
            sleep(1)
            print("You wonder what this is all about.")
            sleep(1)
            print("You can't worry right now, though, because a monster that looks like Medusa jumps out of a corner!")
            # Medusa battle begins.
            Medusa = Enemy('Medusa', [Attack('slash', 5), Attack('bite', 2.5), Attack('smash', 7.5)], 25, ['armor of Paul Revere', 'sword of fire', 'cursed flames'])
            player.HPlimit = 20
            while player.HP > 0.1 and Medusa.HP > 0.1:
                Medusa.attack(player, player.attack(Medusa))
            if player.HP > 0.1:
                print("You vanquished Medusa!")
                drop = random.choice(Medusa.drops)
                print("Medusa dropped 5 healthpotions, too.")
                player.healthpotions += 5
                a = 0
                skeleton = Enemy('skeleton', [Attack('claw', 5, 'None'), Attack('shoot', 7.5, 'Heal')], 15, ['sword', 'sword', 'sparks', 'sparks', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion', 'healthpotion'], None)
                livingjaw = Enemy('living jaw', [Attack('bite', 7.5, 'poison')], 10, ['healthpotion'], None)
        level += 1
    # endgame
    print("You died...")
    print("You killed", monsterskilled, "monsters.")
    print("You got to level", level, ".")

# initiate
DungeonLife()
