#!usr/bin/python
from time import sleep
import random


class universal:
    def __init___(self, ID):  #add any universal variables here
        self.id = ID


universal = universal()
universal.ID = 7


class Item:
    def __init__(self, name, dimensions=["Normal", "Evil"]):
        self.name = name
        if name == 'key':
            self.dimensions = dimensions
        self.ID = universal.ID
        universal.ID += 1

    def use(self, player):
        print('You used', self.name)
        if self.name == 'key':
            player.newlevel = 0
            player.dimensionnumber += 1
            player.dimension = self.dimensions[player.dimensionnumber]
            print(
                "You turn the key in the air and...  WHOOSH!  You are in another dimension..."
            )
        if self.name == 'healthtomb':
            addhealth = round(
                player.HPlimit / 3
            )  # determine how much health will be gained to prevent overflowing
            if player.HP + addhealth > player.HPlimit:
                player.HP = player.HPlimit
            else:
                player.HP += addhealth
        if self.name == 'healthpotion':
            addhealth = round(
                player.HPlimit / 4, 1
            )  # determine how much health will be gained to prevent overflowing
            if player.HP + addhealth > player.HPlimit:
                player.HP = player.HPlimit
            else:
                player.HP += addhealth
        if self.name == 'potion':
            for a in player.effectlist:
                player.effectlist.remove(a)
        if self.name == 'superpotion':
            addhealth = round(player.HPlimit / 4)
            if player.HP + addhealth > player.HPlimit:
                player.HP = player.HPlimit
            else:
                player.HP += addhealth
            for a in player.effectlist:
                player.effectlist.remove(a)
        if self.name == 'snakehair':
            Medusa = Enemy('Medusa', [
                Attack('slash', 2.5, 'None'),
                Attack('bite', 1.5, 'poison'),
                Attack('bash', 3, 'None')
            ], 25, ['armor of Paul Revere', 'poison fang', 'cursed flames'])
            enemy = Medusa
            ran = player.attack(Medusa)
            if enemy.HP > 0.1:
                sleep(1)
                enemy.attack(player, ran)
            if enemy.HP < 0.1:
                enemy.drop(player)
                monsterskilled += 1


# Only ever going to be used for a player.
class Person:
    # initiate
    def __init__(
            self,
            HP,
            attacks,
            HPlimit,
            level=0,
            effectlist=[],
            items={
                1: Item('healthpotion'),
                2: Item('healthpotion'),
                3: Item('healthpotion'),
                4: Item('potion'),
                5: Item('potion'),
                6: Item('potion')
            },
            dimension='Normal',
            dimensionnumber=0):
        self.HP = HP
        self.attacks = attacks
        self.HPlimit = HPlimit
        self.waited = False
        self.effect = "None"
        self.level = level
        self.effectlist = effectlist
        self.items = items
        self.dimension = dimension
        self.dimensionnumber = dimensionnumber

    # this is the attack section
    def attack(self, currentenemy):
        # check for effects
        if 'electricity' in self.effectlist:
            self.HP -= 2
            currentenemy.HP -= 2
            self.effect = 'None'
        if 'heal' in self.effectlist:
            currentenemy.HP += 1
            self.effect = 'None'
        if 'fire' in self.effectlist:
            self.HP -= 1
        if 'cursed fire' in self.effectlist:
            self.HP -= 1.5
        if 'poison' in self.effectlist:
            self.HP -= 2
        import random
        # Ask for what to do?
        if self.HP < 0.1:
            return False
        print("What would you like to do(Attack, Use, Wait, or Flee)?")
        print("You have", self.HP, "HP. ", currentenemy.name, "has",
              currentenemy.HP, "HP.")
        whattodo = input().lower()
        # Attack process
        if whattodo == 'attack':
            print("What attack would you like to use?")
            # print out available attacks
            leave = False
            while not leave:
                for a in self.attacks:
                    print(a)
                attack = input()
                # deal damage
                for a in self.attacks:
                    if a == attack:
                        leave = True
                        print("You use", a, "doing",
                              self.attacks.get(a).damage, "damage.  It has",
                              self.attacks.get(a).effect, "effect.")
                        if not 'shield' in self.effectlist:
                            currentenemy.HP -= self.attacks.get(attack).damage
                            currentenemy.effectlist.append(
                                self.attacks.get(attack).effect)
                            leave = True
                        else:
                            self.effectlist.remove('shield')
                            print("You were blocked!")
            # Healing section
        if whattodo == "use":
            print("You can use:")
            for a in self.items:
                print(self.items.get(a).name)
            whattodo = input()
            for a in self.items:
                if self.items.get(a).name == whattodo:
                    self.items.get(a).use(self)
                    del (self.items[a])
                    break
            if whattodo == 'wait':
                print("You wait for", currentenemy.name,
                      "'s attack, hoping to dodge it.")
                self.waited = True
            if whattodo == 'flee':
                dice = [1, 2]
                import random
                diceroll = random.choice(dice)
                if diceroll == 1:
                    print("You run away, your feet flying.")
                    # variable "run"
                    return True
            return False

    # Function for in between levels
    def between(player, obj):
        print("What would you like to do while you're safe?")
        leave = False
        while not leave:
            whattodo = input().lower()
            if whattodo == "leave":
                leave = True
            if whattodo == 'show':
                print("HP:", player.HP, "/", player.HPlimit)
                print("level:", player.level)
                print("dimension:", player.dimension)
                print("effects:")
                for a in player.effectlist:
                    print(a)
                print("items:")
                for a in player.items:
                    print(player.items.get(a).name)
                print("attacks:")
                for a in player.attacks:
                    print(a)
            if whattodo == 'l3v3l':
                # cheat code
                leave3 = False
                while not leave3:
                    try:
                        player.level = int(input()) - 1
                    except ValueError:
                        continue
                    leave3 = True
            if whattodo == "use":
                print("You can use:")
                for a in player.items:
                    print(player.items.get(a).name)
                whattodo = input()
                for a in player.items:
                    if player.items.get(a).name == whattodo:
                        player.items.get(a).use(player)
                        del (player.items[a])
                        break
            if whattodo == "m4k3":
                #also cheat code
                leave3 = False
                print("drop (as documented in code):")
                randomenemy = Enemy("randomenemy", [], 0, [input()], [])
                print("How many?")
                try:
                    for a in range(0, int(input())):
                        randomenemy.drop(player)
                except ValueError:
                    print("try again...")
            if whattodo == 'load':
                from ast import literal_eval
                print("Paste code onto screen:")
                code = []
                for a in range(0, 8):
                    code.append(input())

                def function_reader(a):
                    x = 0
                    for b in a:
                        if b == "(":
                            parameter_begin = x
                        if b == ")":
                            parameter_end = x
                    return a[parameter_begin + 1:parameter_end]

                def further_reader(a):
                    lst = a.split(',')
                    x = lst[0]
                    y = int(lst[1])
                    z = lst[2]
                    return x, y, z

                HP = int(code[0])
                attacks = {}
                dictionary = literal_eval(code[1])
                for a in dictionary:
                    b = function_reader(dictionary.get(a))
                    attacks[a] = Attack(further_reader(b))
                HPlimit = int(code[2])
                level = int(code[3])
                effectlist = code[4]
                items = code[5]
                dimension = code[6]
                dimensionnumber = int(code[7])
                player = Person(HP, attacks, HPlimit, level, effectlist, items,
                                dimension, dimensionnumber)
                print(type(code))
            if whattodo == 'save':
                code = []
                lst = {}
                for a in player.attacks:
                    b = player.attacks.get(a)
                    sttr = 'Attack('
                    sttr += str(b.name)
                    sttr += ','
                    sttr += str(b.damage)
                    sttr += ','
                    sttr += str(b.effect)
                    sttr += ')'
                    lst[b.name] = sttr
                attacks = lst
                lst = {}
                for a in player.items:
                    b = player.items.get(a)
                    sttr = 'Item('
                    sttr += str(b.name)
                    sttr += ')'
                    lst[b.ID] = sttr
                items = lst
                code.append(player.HP)
                code.append(attacks)
                code.append(player.HPlimit)
                code.append(player.level)
                code.append(player.effectlist)
                code.append(items)
                code.append(player.dimension)
                code.append(player.dimensionnumber)
                for a in code:
                    print(a)
        return player.level + 1, player.dimension, player


# Attack class
class Attack:
    def __init__(self, name, damage, effect):
        self.name = name
        self.damage = damage
        self.effect = effect


# enemies
class Enemy:
    def __init__(self, name, attacks, HP, drops, effectlist):
        self.name = name
        self.attacks = attacks
        self.HP = HP
        self.drops = drops
        self.effectlist = effectlist
        self.HPlimit = HP

    def attack(self, currentperson, ran):
        # check for effects
        if 'electricity' in self.effectlist:
            self.HP -= 2
            currentperson.HP -= 2
            self.effectlist.remove('electricity')
        if 'heal' in self.effectlist:
            currentperson.HP += 5
            self.effectlist.remove('heal')
        if 'fire' in self.effectlist:
            self.HP -= 1
        if 'cursed fire' in self.effectlist:
            self.HP -= 1.5
        if 'poison' in self.effectlist:
            self.HP -= 2
        # attack the player
        attack = random.choice(self.attacks)
        if currentperson.waited != True:
            print(self.name, "used", attack.name, "doing", attack.damage,
                  "damage.  It has", attack.effect, "effect.")
            if not 'shield' in self.effectlist:
                currentperson.HP -= attack.damage
                currentperson.waited = False
                if not attack.effect == 'None':
                    currentperson.effectlist.append(attack.effect)
            else:
                self.effectlist.remove('shield')
                print("But you blocked the attack!")
        else:
            dice = [1, 2]
            diceroll = random.choice(dice)
            if diceroll == 1:
                print(self.name, "missed you while trying to do", attack.name,
                      ".")
            else:
                print(self.name, "used", attack.name, "doing", attack.damage,
                      "damage.  It has", attack.effect, "effect.")
                if not 'shield' in self.effectlist:
                    currentperson.HP -= attack.damage
                    currentperson.waited = False
                    if not attack.effect == 'None':
                        currentperson.effectlist.append(attack.effect)
                else:
                    self.effectlist.remove('shield')
                    print("But you blocked the attack!")

    def drop(self, currentperson, drop=''):
        if drop == '':
            drop = random.choice(self.drops)
        try:
            #=============================ARMORS============================================#
            # drop items
            if drop == 'iron armor':
                if currentperson.HPlimit < 15:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 15
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'steel armor':
                if currentperson.HPlimit < 20:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 20
                    currentperson.HP = HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'orc armor':
                if currentperson.HPlimit < 30:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 30
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'armor of Paul Revere':
                if currentperson.HPlimit < 40:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 40
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'rock armor':
                if currentperson.HPlimit < 65:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 65
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'titanium armor':
                if currentperson.HPlimit < 100:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 100
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'evil armor':
                if currentperson.HPlimit < 120:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 120
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'super armor':
                if currentperson.HPlimit < 1000:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 1000
                    currentperson.HP = currentperson.HPlimit
                    currentperson.HP -= oldHPlimit - oldHP
#======================================================ATTACKS=================================#
            if drop == 'sword':
                sword = Attack('sword', 3.5, 'None')
                currentperson.attacks['sword'] = sword
            if drop == 'rock club':
                club = Attack('club', 10, 'None')
                currentperson.attacks['club'] = club
            if drop == 'poison fang':
                poison_fang = Attack('poison fang', 5, 'poison')
                currentperson.attacks['poison fang'] = poison_fang
            if drop == 'sparks':
                sparks = Attack('sparks', 3, 'electricity')
                currentperson.attacks['sparks'] = sparks
            if drop == 'cursed flames':
                cursed_flames = Attack('cursed flames', 5, 'cursed fire')
                currentperson.attacks['cursed flames'] = cursed_flames
            if drop == 'health tomb':
                health_tomb = Attack('health tomb', 2.5, 'heal')
                currentperson.attacks['health tomb'] = health_tomb
                healthtomb = Item('healthtomb')
                currentperson.items['healthtomb'] = healthtomb
            if drop == "Snape's wand":
                wand = Attack("wand", 7.5, 'None')
                currentperson.attacks['wand'] = wand
            if drop == 'electric staff':
                electricity = Attack('electricity', 10, 'electricity')
                currentperson.attacks['electricity'] = electricity
            if drop == 'fireball':
                fireball = Attack('fireball', 10, 'fire')
                currentperson.attacks['fireball'] = fireball
            if drop == 'plant':
                plant = Attack('plant', 10, 'heal')
                currentperson.attacks['plant'] = plant
            if drop == 'sword of fire':
                firesword = Attack('fire sword', 6, 'fire')
                currentperson.attacks['firesword'] = firesword
            if drop == 'blade of night':
                nightblade = Attack('nightblade', 10, 'shield')
                currentperson.attacks['nightblade'] = nightblade
            if drop == 'instakill':
                instakill = Attack('kill', 1000, 'cursed fire')
                currentperson.attacks['kill'] = instakill
            if drop == 'shield':
                shield = Attack('shield', 0, 'shield')
                currentperson.attacks['shield'] = shield


#=================================ITEMS==================================================================================#
            if drop == 'healthpotion':
                healthpotion = Item('healthpotion')
                currentperson.items[healthpotion.ID] = healthpotion
            if drop == 'key':
                key = Item('key')
                currentperson.items[key.ID] = key
            if drop == 'potion':
                potion = Item('potion')
                currentperson.items[potion.ID] = potion
            if drop == 'superpotion':
                superpotion = Item('superpotion')
                currentperson.items[superpotion.ID] = superpotion
            if drop == 'snakehair':
                snakehair = Item('snakehair')
                currentperson.items[snakehair.ID] = snakehair
            print(self.name, "dropped", drop, ".")
        except NameError:
            print(self.name, "dropped nothing.")


def DungeonLife(
        player=Person(10, {
            'stick': Attack('stick', 1.5, 'None'),
            'fire': Attack('fire', 2.5, 'fire')
        }, 10),
        done=False):
    from time import sleep
    import random
    monsterskilled = 0
    # define enemies
    snake = Enemy('Snake',
                  [Attack('bite', 2, 'poison'),
                   Attack('spit', 1, 'None')], 5, [
                       'iron armor', 'sword', 'healthpotion', 'healthpotion',
                       'healthpotion', 'sparks', 'potion', 'potion', 'potion'
                   ], [])
    spider = Enemy(
        'Spider', [Attack('bite', 2.5, 'poison'),
                   Attack('web', 1.5, 'heal')], 3.5,
        [
            'iron armor', 'sword', 'sparks', 'healthpotion', 'healthpotion',
            'healthpotion', 'potion', 'potion', 'potion'
        ], [])
    snapeminion = Enemy("Snape's minion",
                        [Attack("Avada Kedavra", 10, 'None')], 10,
                        ['healthpotion', 'cursed flames'], [])
    skeleton = Enemy(
        'skeleton', [Attack('claw', 3, 'None'),
                     Attack('shoot', 1, 'Heal')], 15,
        [
            'sword', 'sword', 'sparks', 'sparks', 'sparks', 'healthpotion',
            'healthpotion', 'healthpotion', 'healthpotion', 'potion', 'potion',
            'potion', 'shield', 'shield', 'shield', 'snakehair', 'snakehair'
        ], [])
    livingjaw = Enemy('living jaw', [Attack('bite', 2, 'poison')], 10,
                      ['healthpotion'], [])
    rock = Enemy('Giant Rock',
                 [Attack('smash', 5, 'None'),
                  Attack('shield', 0, 'shield')], 35, [
                      'healthpotion', 'healthpotion', 'healthpotion',
                      'rock club', 'rock armor', 'potion', 'potion', 'potion'
                  ], [])
    eye = Enemy("Eye",
                [Attack('stare', 10, 'None'),
                 Attack('look', 5, 'sheild')], 40, [
                     'superpotion', 'superpotion', 'superpotion', 'evil armor',
                     'blade of night'
                 ], [])
    deathsoul = Enemy(
        "Death Soul",
        [Attack('search', 10, 'heal'),
         Attack('assault', 25, 'cursed fire')], 20,
        ['superpotion', 'evil armor', 'blade of night'], [])
    # Start game
    enemies = [snake, snake, snake, spider, spider]
    if not done:
        print("You wake up in a dungeon, feeling nautious.")
        sleep(1)
        print("You notice you have a stick strapped to your back.")
        sleep(1)
        print("You also realize you can create fire.")
        sleep(1)
        print("You feel the urge to move up, towards the sky!")
        sleep(1)
        print("Good luck, hero!")
        done = False
        player.items = {
            1: Item('healthpotion'),
            2: Item('healthpotion'),
            3: Item('healthpotion'),
            4: Item('potion'),
            5: Item('potion'),
            6: Item('potion')
        }
        sleep(1)
        print("Hello!  I'm your trainer!")
        sleep(1)
        print(
            "I'm here to help you along your way, but make it snappy!  I have other people to get to."
        )
        sleep(1)
        print("Snake jumps out at you!")
        print("What do you want to do?(Wait, Use, Attack, or Flee?")
        print("Snake has 5 HP.  You have 10 HP.")
        sleep(1)
        print("You have health, so why don't you attack?")
        print("Type in 'attack' to attack")
        while not input().lower() == 'attack':
            continue
        print("fire")
        print("stick")
        sleep(1)
        print(
            "Fire sounds like a good attack, probably better than stick, so let's use that."
        )
        sleep(1)
        print("Type in 'fire.'")
        while not input().lower() == 'fire':
            continue
        print("You use fire, doing 2.5 damage and fire effect.")
        print("Snake uses spit, doing 1 damage and None effect.")
        print("What do you want to do?(Wait, Use, Attack, or Flee?")
        print("Snake has 1.5 HP.  You have 9 HP.")
        sleep(1)
        print(
            "Hey, look! ^  Snake is on fire, so he takes 1 damage every turn!")
        print("There are other effects that are different in every way.")
        sleep(2.5)
        print("Let's finish Snake off!  Attack with fire.")
        while not input().lower() == 'attack':
            continue
        print("stick")
        print("fire")
        while not input().lower() == 'fire':
            continue
        print("You use fire, doing 2.5 damage and fire effect.")
        print("Snake dropped healthpotion.")
        sleep(2.5)
        print("We did it!")
        print("What would you like to do while you're safe?")
        sleep(2.5)
        print("Type in 'show' to see how you're doing.")
        while not input().lower() == 'show':
            continue
        print("HP: 8/10")
        print("effects:")
        print("poison")
        print("items:")
        print("potion")
        print("attacks:")
        print("stick")
        print("fire")
        sleep(2.5)
        print(
            "Oh no!  You're poisoned, so you are going to take 2 damage per turn until you use a potion!"
        )
        print("Type in 'use' to get to the 'use' menu.")
        while not input().lower() == 'use':
            continue
        print("potion")
        sleep(1)
        print("Now type in 'potion' to use it.")
        while not input().lower() == 'potion':
            continue
        print("You used, potion.")
        sleep(1)
        print(
            "OK.  You shouldn't have poison now.  I'm going to go, because I have other adventurers to get to."
        )
        sleep(1)
        print("Now type in 'leave' to leave the safe area.")
        while not input().lower() == 'leave':
            continue
        print(
            "Here are some  healthpotions and potions that will help you along the way."
        )
        sleep(1.75)
        print("I've healed you all the way up.")
        sleep(3)
        print(
            "Good luck, hero.....  and remember, the past is not what you think."
        )
        sleep(3)
        print(
            "(YOU): While pondering the message of the random voice, you head onward."
        )
    while player.HP > 0.1:
        if player.dimension == "Evil" and not done:
            enemies = [eye, eye, eye, eye, eye, deathsoul, deathsoul]
            done = True
        sleep(1)
        player.level, player.dimension, player = player.between(player)
        sleep(2.5)
        enemy = random.choice(enemies)
        print(enemy.name, "jumps out at you!")
        while player.HP > 0.1 and enemy.HP > 0.1:
            sleep(1)
            ran = player.attack(enemy)
            if enemy.HP > 0.1 and player.HP > 0.1:
                sleep(1)
                enemy.attack(player, ran)
        # drop system
        if enemy.HP < 0.1:
            enemy.drop(player)
            monsterskilled += 1
            for a in enemies:
                enemies.remove(a)
                enemies.append(a)
        # Medusa boss battle
        if player.level == 15:
            print("You find a stone tablet bearing this message:")
            sleep(1)
            print(
                "\"You terrible man!  You took the lives of countless people and now you shall pay!\""
            )
            sleep(1)
            print("You wonder what this is all about.")
            sleep(1)
            print(
                "You can't worry right now, though, because a monster that looks like Medusa jumps out of a corner!"
            )
            # Medusa battle begins.
            Medusa = Enemy('Medusa', [
                Attack('slash', 2.5, 'None'),
                Attack('bite', 1.5, 'poison'),
                Attack('bash', 3, 'None')
            ], 25, ['armor of Paul Revere', 'poison fang', 'cursed flames'],
                           [])
            while player.HP > 0.1 and Medusa.HP > 0.1:
                ran = player.attack(Medusa)
                if Medusa.HP > 0.1:
                    Medusa.attack(player, ran)
            if player.HP > 0.1:
                # Rewards and unlocks
                print("You vanquished Medusa!")
                Medusa.drop(player)
                print("Medusa dropped 5 healthpotions, too.")
                player.healthpotions += 5
                print("You unlocked new baddies!")
                sleep(1)
                print("Skeleton and Living Jaw unlocked!")
                enemies = [
                    skeleton, skeleton, skeleton, skeleton, skeleton,
                    livingjaw, livingjaw, livingjaw, snake, snake, snake,
                    spider, spider
                ]
        # Snape boss battle
        # Wow does OOP make programming so much easier!
        if player.level == 30:
            sleep(1)
            print("You found yet another tablet!")
            sleep(1)
            print(
                "It says, \"You made it past the last one?  Bah!  You will not beat my next minion.  You shall forever pay for what you did to me and my family!\""
            )
            print(
                "But before you can investigate further, Snape fires something at you!"
            )
            Snape = Enemy('Snape', [
                Attack('magic flames', 3, 'cursed fire'),
                Attack('Avada Kedavra', 7.5, 'None')
            ], 25, ['orc armor', "Snape's wand"], [])
            while player.HP > 0.1 and Snape.HP > 0.1:
                player.attack(Snape)
                if Snape.HP > 0.1:
                    Snape.attack(player)
            if Snape.HP < 0.1:
                Snape.drop(player)
                print("You unlocked new baddies!")
                sleep(1)
                print("Snape's minion unlocked!")
                enemies = [
                    skeleton, skeleton, skeleton, skeleton, skeleton,
                    livingjaw, livingjaw, livingjaw, snake, snake, snake,
                    spider, spider, snapeminion, snapeminion, snapeminion,
                    snapeminion, snapeminion
                ]
        #refill health for enemies
        for a in enemies:
            a.HP = a.HPlimit
        #Groyle boss battle
        if player.level == 45:
            sleep(1)
            print("These tablets can't be a coincidence anymore.")
            sleep(1)
            print(
                "You look at the tablet and are pulled into a different world."
            )
            sleep(1)
            print("You see a big monster in a forest. \"Die!\", it says.")
            sleep(1)
            print("You pull out your weapon and get ready for battle.")
            Groyle = Enemy('Groyle', [Attack('smash', 10, 'None')], 50,
                           ['rock armor', 'rock club'], [])
            while player.HP > 0.1 and Groyle.HP > 0.1:
                player.attack(Groyle)
                if Groyle.HP > 0.1:
                    Groyle.attack(player)
            if Groyle.HP < 0.1:
                Groyle.drop(player)
                sleep(1)
                print("You're glad you got that out of the way.")
                sleep(1)
                print(
                    "You look back at the tablet again and are sucked back into the dungeon."
                )
                sleep(1)
                print("You unlocked new baddies!")
                sleep(1)
                print("Giant Rock unlocked!")
                enemies = [
                    snake, spider, skeleton, skeleton, livingjaw, livingjaw,
                    livingjaw, snapeminion, snapeminion, snapeminion,
                    snapeminion, rock, rock, rock, rock, rock
                ]
        # Four Titans boss battle
        if player.level == 60:
            sleep(1)
            print(
                "As you move to the next room of the dungeon, you think about the Four Titans you read in books."
            )
            sleep(1)
            print(
                "You don't know how you remember this; all you remember is vague images of them while sitting by a warm fireplace."
            )
            sleep(1)
            print("It seems you are regaining your memories.")
            sleep(1)
            print(
                "Before you can think much more on the subject, though, the Four Titans themselves come around the corner!"
            )
            sleep(1)
            Titans = Enemy('The Titans', [
                Attack('Electric Shock', 12, 'electricity'),
                Attack("Fire Blast", 12, 'fire'),
                Attack("Earth Smash", 15, 'None'),
                Attack('Regrowth', 3, 'heal')
            ], 100, ['electric staff', 'fireball', 'titanium armor', 'plant'],
                           [])
            while player.HP > 0.1 and Titans.HP > 0.1:
                player.attack(Titans)
                if Titans.HP > 0.1:
                    Titans.attack(player)
            if Titans.HP < 0.1:
                Titans.drop(player)
                sleep(1)
                print(
                    "By this point, you are so frustrated by these 'minions' that you shout out, 'WHO IS THERE?  WHY ARE YOU DOING THIS TO ME?  I DON'T EVEN RECALL MY PAST!'"
                )
                sleep(2)
                print("A witch pops out of nowhere as soon as you say that.")
                sleep(1)
                print(
                    "'Ah, lovely. You finally decide to open your solemn mouth that once yelled traitorous words."
                )
                sleep(1)
                print(
                    "'You realize that you are down here for a reason, right?")
                sleep(1)
                print(
                    "'You may not know what has happened, but the truth will startle you...'"
                )
                sleep(1)
                print("The witch cackles with an evil laugh and disapears.")
                sleep(1)
                print(
                    "You shout again, 'What did I d-?'  You stumble with the last word as you are sucked into what seems like a dream."
                )
                sleep(2)
                print(
                    "You are on a plane, in the pilot's seat, with a chained man behind you.  'MMM MM MMMMMM!', the pilot says."
                )
                sleep(1)
                print(
                    "You try to do something but realize you are having a flashback."
                )
                sleep(1)
                print(
                    "You push down on the controls as you nose dive into a building..."
                )
                sleep(1)
                print("BOOM!...")
                sleep(3)
                print(
                    "You hear people screaming as everything fades to black..."
                )
                sleep(5)
                print(
                    "When you wake up, you are in the dungeon again, feeling nautious."
                )
                sleep(1)
                print(
                    "Then you are sucked out of the dream and find the four dead titans next to you."
                )
                sleep(1)
                print(
                    "Once you realize what you did, you feel a crushing despair."
                )
                sleep(1)
                print(
                    "And then comes a longing for your wife and children, to apologize for what you have done."
                )
                sleep(1)
                print(
                    "'Jenna', you say, falling to your knees, 'what have I done?'"
                )
                sleep(1)
                print(
                    "You hope the world, especially Jenna, will forgive you for 9/11 if you ever make it out of this rightful punishment alive."
                )
                sleep(1)
        # Clara boss battle
        if player.level == 75:
            print(
                "You hear the cackle of the witch you saw earlier.  You get ready for a fight."
            )
            sleep(1)
            print("She pops out of nowhere.")
            sleep(1)
            print("'You.'  You say, simultaneously.")
            sleep(1)
            print("The witch says, 'I will end you here and now.'")
            Clara = Enemy('Clara', [
                Attack('kill', 20, "None"),
                Attack('Heal', 10, 'heal'),
                Attack('guilt', 25, 'None')
            ], 200, ['key'], [])
            while player.HP > 0.1 and Clara.HP > 0.1:
                player.attack(Clara)
                if Clara.HP > 0.1:
                    Clara.attack(player)
            if Clara.HP < 0.1:
                print(
                    "You feel like you should use the key in the near future.")
                sleep(1)
                print(
                    "You step out onto the surface, but find it is very different."
                )
                sleep(1)
                print(
                    "From the advanced technology you see, you know that it is years after you commited the crime."
                )
                sleep(1)
                print(
                    "You also know no one could have survived for the 200 years that you figure you were asleep."
                )
                sleep(1)
                print(
                    'Tired and defeated, you turn back into your dungeon, the only home you have had and probably will have, and mourn yourself.'
                )
                sleep(10)
                print("Credits:")
                sleep(0.25)
                print("Storyline: Rod Lewis")
                sleep(0.25)
                print("Code: Rod Lewis")
                sleep(0.25)
                print("Game Design: Rod Lewis")
                sleep(0.25)
                print("Testing: Mrs. Weiner's Wizard Wales 2018-2019")
                sleep(0.25)
                print("Special Thanks to:")
                sleep(0.25)
                print('Kelley Weiner')
                sleep(0.25)
                print("Ric Lewis")
                sleep(0.25)
                print("Noah Pasion")
                sleep(0.25)
                print('Finian')
                sleep(0.25)
                print("And YOU, for playing!")
                sleep(5)
                print(
                    "If you would like to continue across dimensions, the game will continue in 25 secs."
                )
                sleep(25)
        if player.level > 15:
            enemies = [
                skeleton, skeleton, skeleton, skeleton, skeleton, livingjaw,
                livingjaw, livingjaw, snake, snake, snake, spider, spider
            ]
        if player.level > 30:
            enemies = [
                skeleton, skeleton, skeleton, skeleton, skeleton, livingjaw,
                livingjaw, livingjaw, snake, snake, snake, spider, spider,
                snapeminion, snapeminion, snapeminion, snapeminion, snapeminion
            ]
        if player.level > 45:
            enemies = [
                snake, spider, skeleton, skeleton, livingjaw, livingjaw,
                livingjaw, snapeminion, snapeminion, snapeminion, snapeminion,
                rock, rock, rock, rock, rock
            ]
    # endgame
    print("You died...")
    print("You killed", monsterskilled, "monsters.")
    print("You got to level", player.level, ".")
    sleep(3)
    print("Continue? Y/N")
    whattodo = input()
    while True:
        if whattodo == 'Y':
            if player.level < 5:
                player.level = 5
            DungeonLife(
                Person(player.HPlimit, player.attacks, player.HPlimit,
                       (player.level - 5), [], player.items, player.dimension,
                       player.dimensionnumber), True)
        elif whattodo == 'N':
            break
        else:
            print("Please input Y or N.")


# initiate
DungeonLife()