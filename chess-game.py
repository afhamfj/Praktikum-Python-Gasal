def setup_board():
    for row in range(8):
        for col in range(8):
            if (row, col) in [(6, col), (7, col)]:
                board[row][col] = 'wp'
            elif (row, col) in [(1, col), (0, col)]:
                board[row][col] = 'bp'
    board[0] = ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br']
    board[7] = ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
def display_board():
    print('   a b c d e f g h')
    for row in range(8):
        print(f'{row+1} {board[row][0]} {board[row][1]} {board[row][2]} {board[row][3]} {board[row][4]} {board[row][5]} {board[row][6]} {board[row][7]}')
def move_piece(start, end):
    board[end[0]][end[1]] = board[start[0]][start[1]]
    board[start[0]][start[1]] = ' '
setup_board()
display_board()

while True:
    start = input("Enter the start position: ")
   