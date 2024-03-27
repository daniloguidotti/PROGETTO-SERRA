import random

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(" ".join(row))

    def place_ship(self, ship_size):
        orientation = random.choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - ship_size)
            for i in range(ship_size):
                self.grid[x][y+i] = 'X'
        else:  # vertical
            x = random.randint(0, self.size - ship_size)
            y = random.randint(0, self.size - 1)
            for i in range(ship_size):
                self.grid[x+i][y] = 'X'

# Esempio di utilizzo
if __name__ == "__main__":
    board_size = 10
    ship_sizes = [5, 4, 3, 3, 2]  # dimensioni delle navi

    game_board = Board(board_size)
    for size in ship_sizes:
        game_board.place_ship(size)

    print("Battaglia Navale")
    print("Legenda:")
    print("O: Mare")
    print("X: Nave")
    print()
    game_board.display()
