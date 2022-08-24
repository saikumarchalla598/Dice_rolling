# -*- coding: utf-8 -*-
"""

@author: Srinu-sai
"""

import random
def parse(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    
def roll_dice(dice_num):
    res = []
    for i in range(dice_num):
        r = random.randint(1,6)
        res.append(r)
    return res

def get_dice_faces(dice_values):
    dice_faces = []
    for i in dice_values:
        dice_faces.append(dice_art[i])
    return dice_faces

def generate_dice_faces_rows(dice_faces):
    dice_facerow = []
    
    for i in range(dice_ht):
        row = []
        
        for die in dice_faces:
            row.append(die[i])
        row_str = " ".join(row)
        dice_facerow.append(row_str)
    wd = len(dice_facerow[0])
    header = " RESULTS ".center(wd, "*")
    dice_faces_diagram = "\n".join([header] + dice_facerow)
        
    return dice_faces_diagram

dice_art = {
    1: (
        "┌─────────┐",        "│         │",        "│    ●    │",        "│         │",        "└─────────┘",    ),
    2: (
        "┌─────────┐",        "│  ●      │",        "│         │",        "│      ●  │",        "└─────────┘",    ),
    3: (
        "┌─────────┐",        "│  ●      │",        "│    ●    │",        "│      ●  │",        "└─────────┘",    ),
    4: (
        "┌─────────┐",        "│  ●   ●  │",        "│         │",        "│  ●   ●  │",        "└─────────┘",    ),
    5: (
        "┌─────────┐",        "│  ●   ●  │",        "│    ●    │",        "│  ●   ●  │",        "└─────────┘",    ),
    6: (
        "┌─────────┐",        "│  ●   ●  │",        "│  ●   ●  │",        "│  ●   ●  │",        "└─────────┘",    ),
}
dice_ht = len(dice_art[1])
dice_wd = len(dice_art[1][0])

dice = input("How many dice do you want to roll(1-10): ")
check = parse(dice)
if check is True:
    dice_num = int(dice)
    if dice_num>0 and dice_num<=10:
        roll_res = roll_dice(dice_num)
        print(roll_res)
        faces = get_dice_faces(roll_res)
        dice_dia = generate_dice_faces_rows(faces)

        print(f"\n{dice_dia}")
    else:
        print('Please enter an integer 1 to 10.')
else:
    print('Please enter an integer.')