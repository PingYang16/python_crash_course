from random import randint

class Die():
    """A Die with attribute called sides"""
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(f"The front of this dice is number {x} now.")

die_6 = Die()
die_6.roll_die()

die_10 = Die(10)
die_10.roll_die()