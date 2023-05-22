import random

ANSWER = int(random.randint(1,9))
HISTORY = []


def guess():
    while True:
        NUM = input('Enter a guess: ').lower()
        if NUM == 'exit':
            break
        while (not NUM.isnumeric()) or (NUM == ''):
            NUM = input('The guess needs to be numaric: ')
        NUM = int(NUM)
        while not (1 <= NUM <= 9):
            NUM = int(input('Enter a guess between 1-9: '))
        while NUM in HISTORY:
            NUM = int(input('You already guessed that number, choose another: '))
        HISTORY.append(NUM)
        print(check_win(NUM))
        if check_win(NUM) == "You're right":
            break


def check_guess():
    pass

def check_win(NUM):
    if ANSWER == NUM:
        return "You're right"
    elif ANSWER < NUM:
        return "You're too high"
    elif ANSWER > NUM:
        return "You're too low"


def main():
    guess()
    print(HISTORY)
    print('GAME OVER!')

if __name__ == "__main__":
    main()