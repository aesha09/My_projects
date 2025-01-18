import random

def roll_dice():
    dice_faces = {
        1: "[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]",
        2: "[-----]\n[ 0   ]\n[     ]\n[   0 ]\n[-----]",
        3: "[-----]\n[     ]\n[0 0 0]\n[     ]\n[-----]",
        4: "[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]",
        5: "[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]",
        6: "[-----]\n[0 0 0]\n[     ]\n[0 0 0]\n[-----]"
    }
    
    return dice_faces[random.randint(1, 6)]

while True:
    print(roll_dice())
    choice = input("Press 'y' to roll again or 'n' to exit: ").strip().lower()
    if choice != 'y':
        break
    print()
