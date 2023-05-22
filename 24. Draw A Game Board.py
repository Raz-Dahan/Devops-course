
def draw_board():
    rows = int(input('how many rows?'))
    columns = int(input('how many columns?'))
    for i in range(rows):
        print(' ---' * columns)
        print('|   ' * (columns + 1))
    print(' ---' * columns)

draw_board()


