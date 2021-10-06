import random


class Dice:
    def roll(self):
        firstNumber = random.randint(1,6)
        secondNumber = random.randint(1,6)
        return firstNumber, secondNumber


dice = Dice()
output = dice.roll()
print(output)