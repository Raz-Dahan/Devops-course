
game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
    ]
    
def user_turn():
    # plyer1
    print('Player 1!')
    location1 = input('Enter your row,colum:').split(',')
    row1 = location1[0]
    col1 = location1[1]
    ans1 = 'X'
    draw(row1, col1, ans1)
    # plyer2
    print('Player 2!')
    location2 = input('Enter your row,colum:').split(',')
    row2 = location2[0]
    col2 = location2[1]
    ans2 = 'O'
    draw(row2, col2, ans2)


def draw(row, col, ans):
    row = int(row) - 1
    col = int(col) - 1
    game[row][col] = ans
    print(game)

# come back to 27 bonus    

print(user_turn()) 

