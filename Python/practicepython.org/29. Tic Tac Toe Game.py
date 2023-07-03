# game is the game table, when 0 represent an empty space
game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
    ]
# history is the old choises
history = []

board_size = 3

def player1_turn():
    """
    a function that ask player 1 for input
    it's also check the user's input
    """
    print("it's player1's turn")
    location = input('Enter your row,column:').split(',')
    while not (1 <= int(location[0]) <= 3 and 1 <= int(location[1]) <= 3):
        location = input('Please give row,column values between 1-3:').split(',')
    while location in history:
        location = input('The cell is full, choose another row,column:').split(',')
    history.append(location)
    row = int(location[0])
    col = int(location[1])
    ans = 'X'
    draw(row, col, ans)

def player2_turn():
    """
    a function that ask player 2 for input
    it's also check the user's input
    """
    print("it's player2's turn")
    location = input('Enter your row,column:').split(',')
    while not (1 <= int(location[0]) <= 3 and 1 <= int(location[1]) <= 3):
        location = input('Please give row,column values between 1-3:').split(',')
    while location in history:
        location = input('The cell is full, choose another row,column:').split(',')
    history.append(location)
    row = int(location[0])
    col = int(location[1])
    ans = 'O'
    draw(row, col, ans)

def draw(row, col, ans):
    """
    a function that draw the game table with the last user's moves
    """
    row = row - 1
    col = col - 1
    game[row][col] = ans
    for list in game:
        print(' --- --- --- ')
        line = ''
        for x in list:
            if x != 0:
                line += '| ' + x + ' '
            elif x == 0:
                line += '|   '
        line += '|'
        print(line)
    print(' --- --- --- ')

def check_win(game):
    return check_row(game) or check_column(game) or check_diagonal(game)

def check_row(game):
    for list in game:
        if len(set(list)) == 1 and list[0] != 0:
            return True
    return False

def check_column(game):
    for i in range(board_size):
        if game[0][i] == game[1][i] == game[2][i] != 0:
            return True
    return False

def check_diagonal(game):
    if game[0][0] == game[1][1] == game[2][2] != 0:
        return True
    elif game[0][2] == game[1][1] == game[2][0] != 0:
        return True
    else:
        return False
    

def main():
    """"
    run the functions as long nobody won,
    if nobody won it's says it's a draw
    """
    times = 0
    while check_win(game) == False:
        if times == 9:
            print("it's a draw!")
            break
        player1_turn()
        if check_win(game) == True:
            print('player1 won!')
            break
        print('\n')
        times += 1
        if times == 9:
            print("it's a draw!")
            break
        player2_turn()
        if check_win(game) == True:
            print('player2 won!')
            break
        print('\n')
        times += 1


if __name__ == "__main__":
    main()
