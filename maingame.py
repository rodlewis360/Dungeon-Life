def DungeonLife():
    import random
    monsterskilled = 0
    from time import sleep
    HP = 10
    HPlimit = 10
    enemies = ['snake', 'snake', 'snake', 'skeleton', 'skeleton', 'spider', 'spider', 'living jaw']
    snakeattacks = ['spit poison', 'bite']
    skeletonattacks = ['claw', 'shoot', 'back up']
    spiderattacks = ['bite', 'climb']
    livingjawattacks = ['bite']
    droppables = ['sword', 'healing potion', 'armor', 'sparks']
    print("You wake up in a dungeon, feeling natious.")
    sleep(2.5)
    print("You wonder why and how you got here, but you cannot worry now, for some reason.")
    sleep(2.5)
    print("You notice that you have a stick strapped to your side.")
    meleeweapon = 'stick'
    sleep(2.5)
    print("You also realize that you can manipulate and create fire.")
    magicweapon = 'fire'
    sleep(2.5)
    print("You have 5 healing potions.")
    healthpotions = 5
    dice = [1, 2]
    level = 0
    while level < 101:
        poisoned = False
        if HP < 0.1:
            break
        sleep(2.5)
        print("Would you like to heal?")
        if input() == 'yes':
            print("How many potions would you like to drink?")
            drink = int(input())
            a = 0
            if drink > healthpotions:
                drink = healthpotions
            healthpotions -= drink
            print("You drink", drink, "health potions.")
            while healthpotions > 0 and a < drink:
                HP += 2.5
                a += 1
                if HP > HPlimit:
                    healthpotions += 1
                    HP -= 2.5
        enemy = ''
        enemy = random.choice(enemies)
        if enemy == 'snake':
            enemieHP = 5
            print("A snake jumps out at you!")
            poisoned = False
            while enemieHP > 0.1:
                if HP < 0.1:
                    break
                if poisoned == True:
                    HP -= 0.5
                sleep(2.5)
                print("What would you like to do (Melee, Wait, Magic, Flee, or Heal)?")
                print("You have", HP, "HP out of", HPlimit,".")
                print("The snake has", enemieHP, "HP left.")
                waited = 0
                whattodo = input()
                if whattodo == 'Flee':
                    if random.choice(dice) == 1:
                        print("You run away, your feet flying.")
                        break
                    else:
                        print("You try to run away, but the snake is blocking the exit.")
                elif whattodo == 'Melee':
                    if meleeweapon == 'stick':
                        print("Your stick bounces off the snake's head, but you think you've done some damage.")
                        enemieHP -= 1
                        print("The snake loses 1 HP")
                    if meleeweapon == 'sword':
                        print("Your sword sends one scale flying, but the snake hisses loudly.")
                        enemieHP -= 2
                        print("The snake loses 2 health.")
                elif whattodo == 'Wait':
                    print("You wait for the snake's attack, hoping to dodge it.")
                    waited = 1
                elif whattodo == 'Magic':
                    if magicweapon == 'fire':
                        print("Your magic burns a hole through the snake.")
                        enemieHP -= 2.5
                        print("The snake loses 2.5 health")
                    if magicweapon == 'sparks':
                        print("Fire or Sparks?")
                        magic = input()
                        if magic == 'Sparks':
                            print("Your sparks fly around the room.  One hits the snake in the eye.")
                            HP -= 0.5
                            enemieHP -= 3
                            print("You lose 0.5 HP and the snake loses 3 HP.")
                            sleep(2.5)
                            print("The snake is unable to fight.")
                            pass
                        if magic == 'Fire':
                            print("Your magic burns a hole through the snake.")
                            enemieHP -= 2.5
                            print("The snake loses 2.5 health")
                elif whattodo == 'Heal':
                    print("You drink 1 health potion.")
                    healthpotions -= 1
                    HP += 2.5
                    if HP > HPlimit:
                        healthpotions += 1
                        HP -= 2.5
                else:
                    print("Remember, Melee, Magic, Wait, or Flee.")
                sleep(2.5)
                if enemieHP < 1:
                    break
                enemyattack = random.choice(snakeattacks)
                if enemyattack == 'spit poison':
                    if waited == 1:
                        if random.choice(dice) == 1:
                            print("The snake spit poison at you.  It doesn't penetrate your skin, though.")
                            HP -= 1
                        else:
                            print("Your stamina from waiting helped you dodge the poison.")
                    else:
                        print("The snake spit poison at you.  It doesn't penetrate your skin, though.")
                        HP -= 1
                if enemyattack == 'bite':
                    if waited == 1:
                        if random.choice(dice) == 1:
                            print("The snake bit you.  The poison sinks into your vains.")
                            HP -= 1
                            poisoned = True
                        else:
                            print("Your stamina from waiting helps you dodge the snake as it lashes out.")
                    else:
                        print("The snake bit you.  The poison sinks into your vains.")
                        HP -= 1
                        poisoned = True
                if not poisoned == True:
                    poisoned = False
            print("You vanquished the snake!")
            drop = random.choice(droppables)
            if drop == 'sword':
                print("You find that the snake has a sword lodged in it from a past hero.  You do not want to think of the terrible fate that he suffered.")
                meleeweapon = 'sword'
            if drop == 'healing potion':
                print("You find a healing potion stuck in the snake's throat.")
                healthpotions += 1
            if drop == 'armor':
                print("The snake swallowed a past hero with armor.  You try not to look as you pull it out.")
                try:
                    armor == 'iron'
                except NameError:
                    armor = 'iron'
                    HP += 5
            if drop == 'sparks':
                print("You find a spellbook that will teach you sparks strapped on the snake's back.")
                magicweapon = 'sparks'
            monsterskilled += 1
        elif enemy == 'spider':
            enemieHP = 2.5
            print("A spider falls from the ceiling!")
            while enemieHP > 0.1:
                if HP < 0.1:
                    break
                sleep(2.5)
                print("What would you like to do (Melee, Wait, Magic, Flee, or Heal)?")
                print("You have", HP, "HP out of", HPlimit,".")
                print("The spider has", enemieHP, "HP left.")
                waited = 0
                whattodo = input()
                if whattodo == 'Flee':
                    if random.choice(dice) == 1:
                        print("You run away, your feet flying.")
                        break
                    else:
                        print("You try to run away, but the spider bites you and you immediately feel tired.")
                elif whattodo == 'Melee':
                    if meleeweapon == 'stick':
                        print("Your stick smashes the spider's leg.")
                        enemieHP -= 1.25
                        print("The spider loses 1.25 HP")
                    if meleeweapon == 'sword':
                        print("Your sword smashes the spider.  It falls to the ground, dead.")
                        enemieHP -= 2.5
                        print("The spider loses 2.5 health.")
                elif whattodo == 'Wait':
                    print("You wait for the spider's attack, hoping to dodge it.")
                    waited = 1
                elif whattodo == 'Magic':
                    if magicweapon == 'fire':
                        print("Your fire misses the spider.")
                        enemieHP -= 0.5
                        print("The spider loses 0.5 health")
                    if magicweapon == 'sparks':
                        print("Fire or Sparks?")
                        magic = input()
                        if magic == 'Sparks':
                            print("Your sparks fly around the room.  The spider falls to the ground.  Looks fried.")
                            HP -= 1.5
                            enemieHP -= 2.5
                            print("You lose 1.5 HP and the spider loses 2.5 HP.")
                            sleep(2.5)
                        if magic == 'Fire':
                            print("Your fire misses the spider.")
                            enemieHP -= 0.5
                            print("The spider loses 0.5 health")
                    print("You drink 1 health potion.")
                    healthpotions -= 1
                    HP += 2.5
                    if HP > HPlimit:
                        healthpotions += 1
                        HP -= 2.5
                else:
                    print("Remember, Melee, Magic, Wait, or Flee.")
                    pass
                sleep(2.5)
                if enemieHP < 1:
                    break
                enemyattack = random.choice(spiderattacks)
                if enemyattack == 'bite':
                    if waited == 1:
                        if random.choice(dice) == 1:
                            print("The spider bit you.  The wound hurts.")
                            HP -= 2
                        else:
                            print("Your stamina from waiting helped you dodge the spider.")
                    else:
                        print("The spider bit you.  The wound hurts.")
                        HP -= 2
                if enemyattack == 'climb':
                    print("The spider climbs up the wall.")
                    enemieHP += 0.5
                    print("The spider gains 0.5 health.")
            print("You vanquished the spider!")
            drop = random.choice(droppables)
            if drop == 'sword':
                print("You see a sword up on a shelf, next to a spider web.")
                meleeweapon = 'sword'
            if drop == 'healing potion':
                print("You find a healing potion on a shelf that the spider had fiercly guarded.")
                healthpotions += 1
            if drop == 'armor':
                print("You find a skeleton wearing iron armor in a corner, riddled with spider webs.")
                try:
                    armor
                except NameError:
                    armor = 'iron'
                    HPlimit = 15
                    HP += 5
            if drop == 'sparks':
                print("You find \"A Teacher's Guide to Teaching Sparks!\" on a shelf.")
                magicweapon = 'sparks'
            monsterskilled += 1
        level += 1
        if level > 14 and enemy != 'snake' and enemy != 'spider':
            enemy = random.choice(['skeleton', 'skeleton', 'living jaw'])
            if enemy == 'skeleton':
                enemieHP = 10
                print("A dead skeleton in the corner of the room gets up.")
                while enemieHP > 0.1:
                    if HP < 0.1:
                        break
                    sleep(2.5)
                    print("What would you like to do (Melee, Wait, Magic, Flee, or Heal)?")
                    print("You have", HP, "HP out of", HPlimit,".")
                    print("The skeleton has", enemieHP, "HP left.")
                    waited = 0
                    whattodo = input()
                    if whattodo == 'Flee':
                        if random.choice(dice) == 1:
                            print("You run away, your feet flying.")
                            break
                        else:
                            print("You try to run away, but the skeleton shoots you in the leg.")
                            HP -= 3.5
                            print("You lose 3.5 HP.")
                    elif whattodo == 'Melee':
                        if meleeweapon == 'stick':
                            print("Your stick bounces off the skeleton's head.")
                            enemieHP -= 0
                            print("The skeleton loses 0 HP")
                        if meleeweapon == 'sword':
                            print("Your sword separates a few bones from the creature.")
                            enemieHP -= 1.75
                            print("The skeleton loses 1.75 health.")
                    elif whattodo == 'Wait':
                        print("You wait for the skeleton's attack, hoping to dodge it.")
                        waited = 1
                    elif whattodo == 'Magic':
                        if magicweapon == 'fire':
                            print("Your fire goes through the skeleton's head.  Melts a bone, though.")
                            enemieHP -= 1
                            print("The skeleton loses 1 health")
                        if magicweapon == 'sparks':
                            print("Fire or Sparks?")
                            magic = input()
                            if magic == 'Sparks':
                                print("Your sparks fly around the room.  The skeleton falls back, hard.")
                                HP -= 1.5
                                enemieHP -= 2.5
                                print("You lose 1.5 HP and the skeleton loses 2.5 HP.")
                                sleep(2.5)
                                continue
                            if magic == 'Fire':
                                print("Your fire goes through the skeleton's head.  Melts a bone, though.")
                                enemieHP -= 1
                                print("The spider loses 1 health")
                        if whattodo == 'Heal':
                            print("You drink 1 health potion.")
                            healthpotions -= 1
                            HP += 2.5
                            if HP > HPlimit:
                                healthpotions += 1
                                HP -= 2.5
                    else:
                        print("Remember, Melee, Magic, Wait, or Flee.")
                        continue
                    sleep(2.5)
                    if enemieHP < 1:
                        break
                    enemyattack = random.choice(skeletonattacks)
                    if enemyattack == 'claw':
                        if waited == 1:
                            if random.choice(dice) == 1:
                                print("The skeleton clawed you.  Your skin turns black where it was punctured.")
                                HP -= 2.5
                            else:
                                print("Your stamina from waiting helped you dodge the skeleton's hand.")
                        else:
                            print("The skeleton clawed you.  Your skin turns black where it was punctured.")
                            HP -= 2
                    if enemyattack == 'back up':
                        print("The skeleton backs out of range.")
                        enemieHP += 01
                        print("The skeleton gains 1 health.")
                print("You vanquished the skeleton!")
                drop = random.choice(droppables)
                if drop == 'sword':
                    print("You see a sword up on a shelf, next to a spider web.")
                    meleeweapon = 'sword'
                if drop == 'healing potion':
                    print("You find a healing potion stick in the skeleton's skull.")
                    healthpotions += 1
                if drop == 'armor':
                    print("You find the skeleton was wearing armor.  The only problem was he put it in his ribcage.")
                    try:
                        armor
                    except NameError:
                        armor = 'steel'
                        HPlimit = 20
                        HP += 10
                        print("You now have an HP limit of 20")
                if drop == 'sparks':
                    print("You find the skeleton's talking brain in a corner.  It's last words were how to make sparks.")
                    magicweapon = 'sparks'
                    print("You unlocked \"Sparks\"!")
        if level == 15:
            print("You find a tablet bearing this message:")
            print("You terrible man!  You took the lives of countless people and now you shall pay!")
            print("You wonder what this is all about.")
    print("You died...")
    print("You killed", monsterskilled, "monsters.")

DungeonLife()
