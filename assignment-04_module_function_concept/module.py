import random
def roll_dice(side):
    return random.randint(1,side)
# print("rolling a 20-side die:", roll_dice(20))
print(f"rolling a 2-dice {roll_dice(2)}")