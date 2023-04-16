import os
import time
import random
import math


def clear():
    os.system('cls')


clear()

# Welcome Message
print("Hello World!")
print("This is a text-rpg prototype \n")
print("Press ENTER to continue")

print(">> ", end = "")
input()

playerHealth = 15
enemyHealth = 50
userInput = ""

player_isDefending = False 

while True:
    clear()
    # Move List
    print("Move List")
    print("  -  Attack (z): Deals Damage")
    print("  -  Heal (x): Heals Back Heath")
    print("  -  Defend (c): Receive 25% less damage on the next attack dealt to you")
    print("  -  Talk (a): Talk to the enemy")
    print("\n")

    # Current Game State
    print(f"Your HP:    {playerHealth}")
    print(f"Enemy HP:   {enemyHealth}")
    print(">> ", end = "")

    userInput = input()

    if userInput == "z":    # Attack Command
        rng = random.randint(2, 5)
        enemyHealth -= rng
        print(f"\nYou attacked the enemy dealing {rng} damage")

    elif userInput == "x":  # Heal Command
        rng = random.randint(2, 4)
        playerHealth += rng

        print(f"\nYou drank your health potion healing back {rng} health")

    elif userInput == "c":  # Defend Command
        player_isDefending = True

        print(f"\nYou form a defensive stance, ready to take a hit")
        time.sleep(1)
        clear()

    elif userInput == "a":  # Talk Command
        print("You asked the enemy how they are doing")
        time.sleep(1)
        clear()
         

    elif userInput == "q":  # Quit Command
        print("Quitting the program. Have a nice day!")
        time.sleep(1)
        clear()
        break

    else:  
        print("\nInvalid command!")
        time.sleep(1)
        continue

    # Enemy "AI"
    time.sleep(0.5)
    rng = random.randint(1, 3)

    if userInput == "a":
        print("The enemy responded, saying that its doing fine but wished that they move moves to do other than attack")
        time.sleep(1.5)
        continue

    if player_isDefending:
        finalValue = rng - (math.floor(rng * .25))
        player_isDefending = False
    else:
        finalValue = rng

    print(f"The enemy attacks you dealing {finalValue}")
    playerHealth -= finalValue
    time.sleep(1)

    # Check Win and Lost Conditions 
    if playerHealth <= 0:
        clear()
        print("DEFEAT!")
        print("Press ENTER to exit")

        print(">> ", end = "")
        input()
        break

    if enemyHealth <= 0:
        clear()
        print("VICTORY!")
        print("Press ENTER to exit")

        print(">> ", end = "")
        input()
        break   