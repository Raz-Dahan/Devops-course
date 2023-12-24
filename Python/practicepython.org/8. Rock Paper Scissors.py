
RED_TEAM = 'RED'
BLUE_TEAM = 'BLUE'

def game():
    while True:
        RED = player_turn(RED_TEAM)
        BLUE = player_turn(BLUE_TEAM)
        
        result = check_win(RED, BLUE)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
    

def player_turn(TEAM):
    print(TEAM + ' team!')
    item = input('Choose your item: ').lower()
    while not (item == 'rock' or item == 'paper' or item == 'scissors'):
        item = input('please choose the rock/paper/scissors options: ').lower()
    return item

def check_win(RED, BLUE):
    if (RED == 'rock' and BLUE == 'scissors') or (RED == 'paper' and BLUE == 'rock') or (RED == 'scissors'and BLUE == 'paper'):
        return 'RED WINS!'
    elif RED == BLUE:
        return "IT'S A TIE!"
    else:
        return 'BLUE WINS!'

print(game())