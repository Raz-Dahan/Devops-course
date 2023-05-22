HISTORY = [2]

def check_guess():
    while True:
        NUM = input('Enter a guess: ').lower()
        if NUM == 'exit':
            break
        while (not NUM.isnumeric()) or (NUM == ''):
            NUM = input('The guess needs to be numaric: ')
        while not (1 <= int(NUM) <= 9):
            NUM = int(input('Enter a guess between 1-9: '))
        while NUM in HISTORY:
            NUM = int(input('You already guessed that number, choose another: '))
    return NUM


check_guess()