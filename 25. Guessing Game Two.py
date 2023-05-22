from random import choice


def game():
    print('Think of a number between 0 to 100 and i\'ll guess it')
    guess = choice(range(0, 101))
    answer = None
    while True:
        answer = input(f'Is it {guess}?(yes/no)').lower
        if answer == 'yes':
            print('Yay i got it!')
            break
        elif answer == 'no':
            answer = input('It\'s higher or lower?(high/low)').lower()
            while True:
                if answer == 'low':
                    guess = guess//2

def search_low(guess):
    pass

game()