import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False

    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False

    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

randomOption = random.randint(1, 3)

if randomOption == 1:
    comp = 's'
elif randomOption == 2:
    comp = 'w'
elif randomOption == 3:
    comp = 'g'

you = input("Your turn! Snake(s), Water(w), Gun(g): ")
a = gameWin(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("Draw game!")

elif a:
    print("You won the game")
else:
    print("You loss the game")
