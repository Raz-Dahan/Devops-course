from random import randrange, choice
from inspect import getsource

YACHT = lambda num, dice: 10 if len(set(dice)) == 1 else 0
ONES = lambda num, dice: 1 if num == 1 else 0
TWOS = lambda num, dice: 2 if num == 2 else 0
THREES = lambda num, dice: 3 if num == 3 else 0
FOURS = lambda num, dice: 4 if num == 4 else 0
FIVES = lambda num,dice: 5 if num == 5 else 0
SIXES = lambda num,dice: 6 if num == 6 else 0
FULL_HOUSE = lambda num, dice: num if (len(set(dice)) == 2 and dice.count(num) == 3) or (len(set(dice)) == 2 and dice.count(num) == 2) else 0
FOUR_OF_A_KIND = lambda num, dice: num if dice.count(num) == 4 else (num*0.8 if dice.count(num) == 5 else 0)
LITTLE_STRAIGHT = lambda num, dice: 6 if sorted(dice) == [1, 2, 3, 4, 5] else 0
BIG_STRAIGHT = lambda num, dice: 6 if sorted(dice) == [2, 3, 4, 5, 6] else 0
CHOICE = lambda num, dice: num


def score(dice, category):
    result = 0
    for num in dice:
        result += category(num, dice)
    return int(result)


dice = [randrange(1, 6) for i in range(5)]
category = choice([YACHT, ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE, FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT, CHOICE])

print('\n')
print(dice)
print(getsource(category))
print(score(dice, category))
print('\n')



def main():
    pass


if __name__ == '__main__':
    main()