import random

class MinesweeperGame:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.is_game_over = False

    def initialize_board(self, first_move_row, first_move_col):
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        positions.remove((first_move_row, first_move_col))
        self.mine_positions = set(random.sample(positions, self.num_mines))

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def count_adjacent_mines(self, row, col):
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                new_row = row + dr
                new_col = col + dc
                if self.is_valid_position(new_row, new_col) and (new_row, new_col) in self.mine_positions:
                    count += 1
        return count

    def reveal_board(self, row, col):
        if self.is_valid_position(row, col) and self.board[row][col] == ' ':
            if (row, col) in self.mine_positions:
                self.is_game_over = True
                self.board[row][col] = 'X'
            else:
                count = self.count_adjacent_mines(row, col)
                self.board[row][col] = str(count) if count > 0 else ' '
                if count == 0:
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if dr == 0 and dc == 0:
                                continue
                            new_row = row + dr
                            new_col = col + dc
                            self.reveal_board(new_row, new_col)

    def print_board(self, show_mines=False):
        print('   ' + ' '.join(str(i) for i in range(self.cols)))
        print('  +' + '--' * self.cols + '+')
        for i, row in enumerate(self.board):
            print(f'{i} | ' + ' '.join(cell if cell != 'X' or show_mines else ' ' for cell in row) + ' |')
        print('  +' + '--' * self.cols + '+')

def play_minesweeper():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    num_mines = int(input("Введите количество мин: "))

    game = MinesweeperGame(rows, cols, num_mines)
    first_move_row = int(input("Введите номер строки первого хода: "))
    first_move_col = int(input("Введите номер столбца первого хода: "))
    game.initialize_board(first_move_row, first_move_col)

    while not game.is_game_over:
        game.print_board()
        row = int(input("Введите номер строки: "))
        col = int(input("Введите номер столбца: "))
        game.reveal_board(row, col)

    print("Игра окончена!")
    game.print_board(show_mines=True)

play_minesweeper()