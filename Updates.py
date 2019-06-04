from time import sleep
import random
# Only ever going to be used for a player.
class Person:
    # initiate
    def __init__(self, HP, attacks, HPlimit, healthpotions, waited, effect, level):
        self.HP = HP
        self.attacks = attacks
        self.HPlimit = HPlimit
        self.healthpotions = healthpotions
        self.waited = waited
        self.effect = effect
        self.level = level
    # this is the attack section
    def attack(self, currentenemy):
        # check for effects
        try:
            if self.effect == 'fire':
                self.HP -= 1
            if self.effect == 'poison':
                self.HP -= 0.5
            if self.effect == 'cursed fire':
                self.HP -= 1.5
            if self.effect == 'electricity':
                self.HP -= 2
                currentenemy.HP -= 0.5
                self.effect = 'None'
            if self.effect == 'heal':
                currentenemy.HP += 0.5
                self.effect = 'None'
        except NameError:
            self.effect = 'None'
        import random
        # Ask for what to do?
        print("What would you like to do(Attack, Heal, Wait, or Flee)?")
        print("You have", self.HP, "HP. ", currentenemy.name, "has", currentenemy.HP, "HP.")
        whattodo = input()
        # Attack process
        if whattodo == 'Attack':
            print("What attack would you like to use?")
            # print out available attacks
            for a in self.attacks:
                print(a)
            attack = input()
            # deal damage
            for a in self.attacks:
                if a == attack:
                    print("You use", a, "doing", self.attacks.get(a).damage, "damage.  It has", self.attacks.get(a).effect, "effect.")
                    currentenemy.HP -= self.attacks.get(attack).damage
                    currentenemy.effect = self.attacks.get(attack).effect
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
    # Fuction for in between levels
    def between(player, obj):
        print("What would you like to do while you're safe?")
        whattodo = input()
        if whattodo == 'show':
            # show stuff
            print("HP:", player.HP)
            print("HP limit:", player.HPlimit)
            print("attacks:")
            for a in player.attacks:
                print(a)
        if whattodo == 'heal':
            print("How many potions would you like to drink?")
            try:
                drink = int(input())
                # drink said number of healthpotions
                if drink > player.healthpotions:
                    drink = player.healthpotions
                player.HP += drink * 2.5
        if whattodo == 'l3v3l':
            player.level = input() - 1
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
        # check for effects and deal damage accordingly
        if self.effect == 'poison':
            self.HP -= 0.5
        if self.effect == 'fire':
            self.HP -= 1
        if self.effect == 'cursed fire':
            self.HP -= 1.5
        if self.effect == 'electricity':
            self.HP -= 2
            currentperson.HP -= 0.5
            self.effect = 'None'
        if self.effect == 'heal':
            currentperson.HP += 1.5
            self.effect = 'None'
        # attack the player
        attack = random.choice(self.attacks)
        if currentperson.waited != True:
            print(self.name, "used", attack.name, "doing", attack.damage, "damage.  It has", attack.effect, "effect.")
            currentperson.HP -= attack.damage
            currentperson.waited = False
            currentperson.effect = attack.effect
        else:
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
                    currentperson.HPlimit = 15
            if drop == 'steel armor':
                if currentperson.HPlimit < 20:
                    currentperson.HPlimit = 20
            if drop == 'orc armor':
                if currentperson.HPlimit < 30:
                    currentperson.HPlimit = 30
            if drop == 'armor of Paul Revere':
                if currentperson.HPlimit < 40:
                    currentperson.HPlimit = 40
            if drop == 'sword':
                sword = Attack('sword', 3.5, 'None')
                currentperson.attacks['sword'] = sword
            if drop == 'poison fang':
                poison_fang = Attack('poison fang', 5, 'poison')
                currentperson.attacks['poison fang'] = poison_fang
            if drop == 'sparks':
                sparks = Attack('sparks', 3, 'electricity')
                currentperson.attacks['sparks'] = sparks
            if drop == 'cursed flames':
                cursed_flames = Attack('cursed flames', 7.5, 'cursed fire')
                currentperson.attacks['cursed flames'] = cursed_flames
            if drop == "Snape's wand":
                snapewand = Attack('Avada Kedavra', 10, 'None')
                currentperson.attacks["Snape's wand"] = snapewand
            if drop == 'healthpotion':
                currentperson.healthpotions += 1
            if drop == 'health tomb':
                health_tomb = Attack('health tomb', 0, 'heal')
                currentperson.attacks['health tomb'] = health_tomb
            print(self.name, "dropped", drop, ".")
        except NameError:
            print(self.name, "dropped nothing.")

def DungeonLife():
    player = Person(10, { 'stick': Attack('stick', 1.5, 'None'), 'fire': Attack('fire', 2.5, 'fire')}, 10, 5, False, 'None', 0)
    from time import sleep
    import random
    monsterskilled = 0
    # define 'snake' and 'spider'
    snake = Enemy('Snake', [Attack('bite', 2.5, 'poison'), Attack('spit', 1, 'None')], 5, ['iron armor', 'sword', 'healthpotion', 'healthpotion', 'healthpotion', 'sparks'], 'None')
    spider = Enemy('Spider', [Attack('bite', 2.5, 'poison'), Attack('web', 1.5, 'heal')], 2.5, ['iron armor', 'sword', 'sparks', 'healthpotion', 'healthpotion', 'healthpotion'], 'None')
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
        if player.HP > 0.1:
            player.level += 1
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
            Snape = Enemy('Snape', [Attack('magic flames', 5, 'cursed fire'), Attack('Avada Kedavra', 10, 'None')], 25, ['orc armor', "Snape's wand"]
            while player.HP > 0.1 and Snape.HP > 0.1:
                player.attack(Snape)
                if Snape.HP > 0.1:
                    Snape.attack(player)
            if Snape.HP < 0.1:
                Snape.drop()
                print("You unlocked new baddies!")
                sleep(1)
                print("Snape's minion unlocked!")
                snapeminion = Enemy("Snape's minion", [Attack("Avada Kedavra", 10, 'None')], 5, ['healthpotion', 'cursed flames']
                enemies.append(snapeminion)
        for a in enemies:
            a.HP = a.HPlimit
    # endgame
    print("You died...")
    print("You killed", monsterskilled, "monsters.")
    print("You got to level", player.level, ".")

# initiate
DungeonLife()
