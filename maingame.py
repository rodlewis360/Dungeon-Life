def DungeonLife():
    import random
    monsterskilled = 0
    from time import sleep
    HP = 10
    HPlimit = 10
    enemies = ['snake', 'skeleton', 'spider', 'living jaw']
    snakeattacks = ['spit poison', 'bite']
    skeletonattacks = ['claw', 'shoot', 'back up']
    spiderattacks = ['bite', 'climb']
    livingjawattacks = ['bite']
    droppables = ['sword', 'healing potion', 'armor']
    print("You wake up in a dungeon, feeling natious.")
    sleep(2.5)
    print("You wonder why and how you got here, but you cannot worry now, for some reason.")
    armor = ''
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
    while True:
        if HP < 1:
            break
        if armor == 'armor':
            HPlimit = 25
            HP += 15
        sleep(2.5)
        print("Would you like to heal?")
        if input() == 'yes':
            print("How many potions would you like to drink?")
            drink = input()
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
        enemy = random.choice(enemies)
        enemy = 'snake'
        if enemy == 'snake':
            enemieHP = 5
            print("A snake jumps out at you!")
            poisoned = False
            while enemieHP > 0:
                if HP < 1:
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
                    print("Your magic burns a hole through the snake.")
                    enemieHP -= 2.5
                    print("The snake loses 2.5 health")
                elif whattodo == 'Heal':
                    print("You drink 1 health potion.")
                    healthpotions -= 1
                    HP += 2.5
                else:
                    print("Remember, Melee, Magic, Wait, or Flee.")
                sleep(2.5)
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
                armor = 'armor'
            monsterskilled += 1
        print("You died...")
        print("You killed", monsterskilled, "monsters.")
        
                
