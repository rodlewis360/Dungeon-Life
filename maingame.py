from time import sleep
import random
# Only ever going to be used for a player.
class Person:
    # initiate
    def __init__(self, HP, attacks, HPlimit, healthpotions, waited, effect, effectlist, level):
        self.HP = HP
        self.attacks = attacks
        self.HPlimit = HPlimit
        self.healthpotions = healthpotions
        self.waited = waited
        self.effect = effect
        self.level = level
        self.effectlist = effectlist 
    # this is the attack section
    def attack(self, currentenemy):
        # check for effects
        try:
            if self.effect == 'fire':
                effectlist.append('fire')
            if self.effect == 'poison':
                effectlist.append('poison')
            if self.effect == 'cursed fire':
                effectlist.append('cursed fire')
            if self.effect == 'electricity':
                self.HP -= 2
                currentenemy.HP -= 2
                self.effect = 'None'
            if self.effect == 'heal':
                currentenemy.HP += 0.5
                self.effect = 'None'
        except NameError:
            pass
        if 'fire' in effectlist:
            self.HP -= 1
        if 'cursed fire' in effectlist:
            self.HP -= 1.5
        if 'poison' in effectlist:
            self.HP -= 0.5
        import random
        # Ask for what to do?
        print("What would you like to do(Attack, Heal, Wait, or Flee)?")
        print("You have", self.HP, "HP. ", currentenemy.name, "has", currentenemy.HP, "HP.")
        whattodo = input()
        # Attack process
        if whattodo == 'Attack':
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
                    print("You use", a, "doing", self.attacks.get(a).damage, "damage.  It has", self.attacks.get(a).effect, "effect.")
                    if not self.effect == "shield":
                        currentenemy.HP -= self.attacks.get(attack).damage
                        currentenemy.effect = self.attacks.get(attack).effect
                    else:
                        self.effect = "None"
        # Healing section
        if whattodo == 'Heal':
            if self.HP + 2.5 > self.HPlimit:
                print("You have too much health.")
            else:
                print("You drink 1 health potion.")
                self.HP += 2.5
                self.healthpotions -= 1
        if whattodo == 'Wait':
            print("You wait for", currentenemy.name, "'s attack, hoping to dodge it.")
            self.waited = True
        if whattodo == 'Flee':
            dice = [1, 2]
            import random
            diceroll = random.choice(dice)
            if diceroll == 1:
                print("You run away, your feet flying.")
                # variable "run"
                return True
        return False
    # Fuction for in between levels
    def between(player, obj):
        print("What would you like to do while you're safe?")
        leave = False
        while not leave:
            whattodo = input()
            if whattodo == "leave":
                leave = True
            if whattodo == 'show':
                # show stuff
                print("HP:", player.HP)
                print("HP limit:", player.HPlimit)
                print("healthpotions:", player.healthpotions)
                print("level:", player.level)
                print("attacks:")
                for a in player.attacks:
                    print(a)
            if whattodo == 'Heal':
                leave2 = False
                print("HP:", player.HP)
                print("healthpotions:", player.healthpotions)
                while not leave2:
                    try:
                        print("How many potions would you like to drink?")
                        drink = int(input())
                        # drink said number of healthpotions
                        if drink > player.healthpotions:
                            drink = player.healthpotions
                        if not player.HP > player.HPlimit:
                            print("You drink", drink, "health potions.")
                            player.HP += drink * 2.5
                            leave2 = True
                        else:
                            print("You have too much health!")
                    except ValueError:
                        print("Input a number!")
            if whattodo == 'l3v3l':
                leave3 = False
                while not leave3:
                    try:
                        player.level = int(input()) - 1
                    except ValueError:
                        continue
                    leave3 = True
        return player.level + 1

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
        self.HPlimit = HP
    def attack(self, currentperson, ran):
        # check for effects
        try:
            if self.effect == 'fire':
                effectlist.append('fire')
            if self.effect == 'poison':
                effectlist.append('poison')
            if self.effect == 'cursed fire':
                effectlist.append('cursed fire')
            if self.effect == 'electricity':
                self.HP -= 2
                currentperson.HP -= 2
                self.effect = 'None'
            if self.effect == 'heal':
                currentperson.HP += 5
                self.effect = 'None'
        except NameError:
            pass
        if 'fire' in effectlist:
            self.HP -= 1
        if 'cursed fire' in effectlist:
            self.HP -= 1.5
        if 'poison' in effectlist:
            self.HP -= 0.5
        # attack the player
        attack = random.choice(self.attacks)
        if currentperson.waited != True:
            print(self.name, "used", attack.name, "doing", attack.damage, "damage.  It has", attack.effect, "effect.")
            if not self.effect == 'shield':
                currentperson.HP -= attack.damage
                currentperson.waited = False
                currentperson.effect = attack.effect
            else:
                self.effect = 'None'
        else:
            dice = [1, 2]
            diceroll = random.choice(dice)
            if diceroll == 1:
                print(self.name, "missed you while trying to do", attack.name, ".")
            else:
                print(self.name, "used", attack.name, "doing", attack.damage, "damage.")
                currentperson.HP -= attack.damage
                currentperson.effect = attack.effect
    def drop(self, currentperson):
        try:
            drop = random.choice(self.drops)
            # drop effects
            if drop == 'iron armor':
                if currentperson.HPlimit < 15:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 15
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'steel armor':
                if currentperson.HPlimit < 20:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 20
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'orc armor':
                if currentperson.HPlimit < 30:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 30
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'armor of Paul Revere':
                if currentperson.HPlimit < 40:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 40
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'rock armor':
                if currentperson.HPlimit < 65:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 65
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'titanium armor':
                if currentperson.HPlimit < 100:
                    oldHPlimit = currentperson.HPlimit
                    oldHP = currentperson.HP
                    currentperson.HPlimit = 100
                    currentperson.HP += HPlimit - HP
                    currentperson.HP -= oldHPlimit - oldHP
            if drop == 'sword':
                sword = Attack('sword', 3.5, 'None')
                currentperson.attacks['sword'] = sword
            if drop == 'rock club':
                club = Attack('club', 10, 'None')
                currentperson.attacks['club' = club]
            if drop == 'poison fang':
                poison_fang = Attack('poison fang', 5, 'poison')
                currentperson.attacks['poison fang'] = poison_fang
            if drop == 'sparks':
                sparks = Attack('sparks', 3, 'electricity')
                currentperson.attacks['sparks'] = sparks
            if drop == 'cursed flames':
                cursed_flames = Attack('cursed flames', 7.5, 'cursed fire')
                currentperson.attacks['cursed flames'] = cursed_flames
            if drop == 'healthpotion':
                currentperson.healthpotions += 1
            if drop == 'health tomb':
                health_tomb = Attack('health tomb', 5, 'heal')
                currentperson.attacks['health tomb'] = health_tomb
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
                plant = Attack('plant', 10, 'shield')
                currentperson.attacks['plant'] = plant
            print(self.name, "dropped", drop, ".")
        except NameError:
            print(self.name, "dropped nothing.")

def DungeonLife():
    player = Person(10, { 'stick': Attack('stick', 1.5, 'None'), 'fire': Attack('fire', 2.5, 'fire')}, 10, 5, False, 'None', 0)
    from time import sleep
    import random
    monsterskilled = 0
    # define 'snake' and 'spider'
    snake = Enemy('Snake', [Attack('bite', 2, 'poison'), Attack('spit', 1, 'None')], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks'], 'None')
    spider = Enemy('Spider', [Attack('bite', 2.5, 'poison'), Attack('web', 1.5, 'heal')], 3.5, ['iron armor', 'sword', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion'], 'None')
    # Start game
    enemies = [snake, snake, snake, spider, spider]
    print("You wake up in a dungeon, feeling nautious.")
    sleep(1)
    print("You notice you have a stick strapped to your back.")
    sleep(1)
    print("You also realize you can create fire and you have 5 health potions.")
    sleep(1)
    print("You feel the urge to move up, towards the sky!")
    sleep(1)
    print("Good luck, hero!")
    while player.HP > 0.1:
        sleep(1)
        player.level = player.between(player)
        sleep(2.5)
        enemy = random.choice(enemies)
        print(enemy.name, "jumps out at you!")
        while player.HP > 0.1 and enemy.HP > 0.1:
            sleep(1)
            ran = player.attack(enemy)
            if enemy.HP > 0.1:
                sleep(1)
                enemy.attack(player, ran)
        # drop system
        if enemy.HP < 0.1:
            enemy.drop(player)
        # Medusa boss battle
        if player.level == 15:
            print("You find a tablet bearing this message:")
            sleep(1)
            print("\"You terrible man!  You took the lives of countless people and now you shall pay!\"")
            sleep(1)
            print("You wonder what this is all about.")
            sleep(1)
            print("You can't worry right now, though, because a monster that looks like Medusa jumps out of a corner!")
            # Medusa battle begins.
            Medusa = Enemy('Medusa', [Attack('slash', 5), Attack('bite', 2.5), Attack('smash', 7.5)], 25, ['armor of Paul Revere', 'sword of fire', 'cursed flames'], 'None')
            while player.HP > 0.1 and Medusa.HP > 0.1:
                Medusa.attack(player, player.attack(Medusa))
            if player.HP > 0.1:
                # Rewards and unlocks
                print("You vanquished Medusa!")
                drop = random.choice(Medusa.drops)
                print("Medusa dropped 5 healthpotions, too.")
                player.healthpotions += 5
                a = 0
                print("You unlocked new baddies!")
                sleep(1)
                print("Skeleton and Living Jaw unlocked!")
                skeleton = Enemy('skeleton', [Attack('claw', 5, 'None'), Attack('shoot', 7.5, 'Heal')], 15, ['sword', 'sword', 'sparks', 'sparks', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion', 'healthpotion'], 'None')
                livingjaw = Enemy('living jaw', [Attack('bite', 7.5, 'poison')], 10, ['healthpotion'], 'None')
                enemies = [skeleton, skeleton, skeleton, skeleton, skeleton, livingjaw, livingjaw, livingjaw, snake, snake, snake, spider, spider]
        # Snape boss battle
        # Wow does OOP make programming so much easier!
        if player.level == 30:
            sleep(1)
            print("You found yet another tablet!")
            sleep(1)
            print("It says, \"You made it past the last one?  Bah!  You will not beat my next minion.  You shall forever pay for what you did to me and my family!\"")
            Snape = Enemy('Snape', [Attack('magic flames', 5, 'cursed fire'), Attack('Avada Kedavra', 10, 'None')], 25, ['orc armor', "Snape's wand"])
            while player.HP > 0.1 and Snape.HP > 0.1:
                player.attack(Snape)
                if Snape.HP > 0.1:
                    Snape.attack(player)
            if Snape.HP < 0.1:
                Snape.drop()
                print("You unlocked new baddies!")
                sleep(1)
                print("Snape's minion unlocked!")
                snapeminion = Enemy("Snape's minion", [Attack("Avada Kedavra", 10, 'None')], 10, ['healthpotion', 'cursed flames'])
                enemies.append(snapeminion)
        #refill health for enemies
        for a in enemies:
            a.HP = a.HPlimit
        #Groyle boss battle
        if player.level = 45:
            sleep(1)
            print("These tablets can't be a coincidence anymore.")
            sleep(1)
            print("You look at the tablet and are pulled into a different world.")
            sleep(1)
            print("You see a big monster in a forest. \"Die!\", it says.")
            sleep(1)
            print("You pull out your weapon and get ready for battle.")
            Groyle = Enemy('Groyle', [Attack('smash', 10, 'None')], 50, ['rock armor', 'rock club'], 'None')
            while player.HP > 0.1 and Groyle.HP > 0.1:
                player.attack(Groyle)
                if Groyle.HP > 0.1:
                    Groyle.attack(player)
            if Groyle.HP < 0.1:
                Groyle.drop()
                sleep(1)
                print("You're glad you got that out of the way.")
                sleep(1)
                print("You look back at the tablet again and are sucked back into the dungeon.")
                sleep(1)
                print("You unlocked new baddies!")
                sleep(1)
                print("Giant Rock unlocked!")
                rock = Enemy('Giant Rock', [Attack('smash', 5, 'None'), Attack('shield', 0, 'shield')])
                enemies = [snake, spider, skeleton, skeleton, livingjaw, livingjaw, livingjaw, snapeminion, snapeminion, snapeminion, snapeminion, rock, rock, rock, rock, rock]
        # Four Titans boss battle
        if player.level == 60:
            sleep(1)
            print("As you move to the next room of the dungeon, you think about the Four Titans you read in books.")
            sleep(1)
            print("You don't know how you remember this; all you remember is vague images of them while sitting by a warm fireplace.")
            sleep(1)
            print("It seems you are regaining your memories.")
            sleep(1)
            print("Before you can think much more on the subject, though, the Four Titans themselves come around the corner!")
            sleep(1)
            Titans = Enemy('The Titans',[Attack('Electric Shock', 12, 'electricity'), Attack("Fire Blast", 12, 'fire'), Attack("Earth Smash", 15, 'None'), Attack('Regrowth', 3, 'heal')], 100, ['electric staff', 'fireball', 'titanium armor', 'plant'], 'None')
            while player.HP > 0.1 and Titans.HP > 0.1:
                player.attack(Titans)
                if Titans.HP > 0.1:
                    Titans.attack(player)
            if Titans.HP > 0.1:
                Titans.drop()
                sleep(1)
                print("By this point, you are so frustrated by these 'minions' that you shout out, 'WHO IS THERE?  WHY ARE YOU DOING THIS TO ME?  I DON'T EVEN RECALL MY PAST!'")
                sleep(2)
                print("A witch pops out of nowhere as soon as you say that.")
                sleep(1)
                print("'Ah, lovely. You finally decide to open your solemn mouth that once yelled traitorous words.")
                sleep(1)
                print("'You realize that you are down here for a reason, right?")
                sleep(1)
                print("'You may not know what is or has happened, but the truth will startle you...'")
                sleep(1)
                print("The witch cackles with an evil laugh and disapears.")
                sleep(1)
                print("You shout again, 'What did I d-', you stumble with the last word as you are sucked into what seems like a dream.")
                sleep(2)
                print("You are on a plane, in the pilot's seat, with a chained man behind you.  'MMM MM MMMMMM!', the pilot says.")
                sleep(1)
                print("You try to do something but realize you are having a flashback.")
                sleep(1)
                print("You push down on the controls as you nose dive into a building...")
                sleep(1)
                print("BOOM!...")
                sleep(3)
                print("You hear people screaming as everything fades to black...")
                sleep(5)
                print("When you wake up, you are in the dungeon again, feeling nautious.")
                sleep(1)
                print("Then you are sucked out of the dream and find the four dead titans next to you.")
                sleep(1)
                print("Once you realize what you did, you feel a crushing despair.")
                sleep(1)
                print("And then comes a longing for your wife and children, to apologize for what you have done.")
                sleep(1)
                print("'Jenna', you say, falling to your knees, 'what have I done?'")
                sleep(1)
                print("You hope the world, especially Jenna, will forgive you for 9/11 if you ever make it out of this rightful punishment alive.")
                sleep(1)
    # endgame
    print("You died...")
    print("You killed", monsterskilled, "monsters.")
    print("You got to level", player.level, ".")

# initiate
DungeonLife()
