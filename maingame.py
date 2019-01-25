def DungeonLife():
    import random
    from time import sleep
    HP = 10
    HPlimit = 10
    enemies = ['snake', 'skeleton', 'spider', 'living jaw']
    snakeattacks = ['spit poison']
    skeletonattacks = ['claw', 'shoot', 'back up']
    spiderattacks = ['bite', 'climb']
    livingjawattacks = ['bite']
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
    healingpotions = 5
    dice = [1,2]
    while True:
        sleep(2.5)
        enemy = random.choice(enemies)
        enemy = 'snake'
        if enemy == 'snake':
            enemieHP = 5
            print("A snake jumps out at you!")
            while enemieHP > 0:
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
                    print("Your", meleeweapon, "bounces off the snake's head, but you think you've done some damage.")
                    if meleeweapon == 'stick':
                        enemieHP -= 1
                        print("The snake loses 1 HP")
                elif whattodo == 'Wait':
                    print("You wait for the snake's attack, hoping to dodge it.")
                    waited = 1
                elif whattodo == 'Magic':
                    print("Your magic burns a hole throught the snake.")
                    enemieHP -= 2.5
                    print("The snake loses 2.5 health")
                elif whattodo == 'Heal':
                    print("You drink 1 health potion.")
                    healthpotions -= 1
                    HP += 2.5
                else:
                    print("Remember, Melee, Magic, Wait, or Flee.")
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
                print("You vanquished the snake!")
