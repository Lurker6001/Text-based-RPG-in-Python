import os
import time
import random

def clear():
    os.system('cls')


clear()

print("Hello World!")
print("This is a text-rpg prototype \n")
print("Press ENTER to continue")

print(">> ", end = "")
input()

playerHealth = 10
enemyHealth = 25
userInput = ""

while True:
    clear()
    print("Move List")
    print("  -  Attack (z): Deals Damage")
    print("  -  Heal (x): Heals Back Heath")
    print("\n")
    print(f"Your HP:    {playerHealth}")
    print(f"Enemy HP:   {enemyHealth}")
    print(">> ", end = "")

    userInput = input()

    if userInput == "z":
        rng = random.randint(2, 5)
        enemyHealth -= rng
        print(f"\nYou attacked the enemy dealing {rng} damage")
    elif userInput == "x":
        rng = random.randint(2, 4)
        playerHealth += rng
        print(f"\nYou drank your health potion healing back {rng} health")
    else:
        print("\nInvalid command!")
        time.sleep(1.5)
        break

    time.sleep(1.5)
    rng = random.randint(1, 3)
    print(f"The enemy attacks you dealing {rng}")
    playerHealth -= rng
    time.sleep(2)

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