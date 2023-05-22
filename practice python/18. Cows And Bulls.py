import random
answer_int = random.randint(1000,9999)
answer = [int(x) for x in str(answer_int)]


def game():
    tries = 0
    while True:
        guess_input = user_input()
        guess = [int(x) for x in guess_input]
        cows = 0
        bulls = 0
        for i in range(4):
            if ( guess[i] in answer ) and ( guess[i] == answer[i] ):
                cows += 1
            elif ( guess[i] in answer ) and ( guess[i] != answer[i] ):
                bulls += 1
        print(str(cows) + ' cows, ' + str(bulls) + ' bulls')
        tries += 1
        if cows == 4:
            print('You got it! \nin ' + str(tries) + ' tries' + '\nGAME OVER')
            break

def user_input():
    guess_input = input('Enter a 4-digit number: ')
    while not (guess_input.isnumeric() and len(guess_input) == 4):
        guess_input = input('The guess must be 4 digits numaric: ')
    return guess_input

def main():
    print('Welcome to the Cows and Bulls Game!')
    game()

if __name__ == "__main__":
    main()