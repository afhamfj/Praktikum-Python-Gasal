class ChessBoard:
    def __init__(self):
        self.board = []
        self.generate_board()

    def generate_board(self):
        # We use ASCII values to represent the board
        for i in range(8):
            row = []
            for j in range(8):
                if (i+j)%2 == 0:
                    row.append("O") # Use "O" to represent black squares
                else:
                    row.append("X") # Use "X" to represent white squares
            self.board.append(row)