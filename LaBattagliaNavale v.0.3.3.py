import tkinter as tk
from tkinter import simpledialog
import random

GRID_SIZE = 10

# Определение кораблей и их длины
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.grid_player = self.create_empty_grid(GRID_SIZE)
        self.grid_computer = self.create_empty_grid(GRID_SIZE)
        self.ship_index = 0
        self.selected_direction = "H"
        self.game_active = False
        self.ship_lengths = list(ships.values())
        self.ship_names = list(ships.keys())
        self.ship_labels = {}
        self.root.withdraw()
        self.show_instructions()

    def create_empty_grid(self, size):
        return [["~" for _ in range(size)] for _ in range(size)]

    def can_place_ship(self, grid, ship_length, row, col, direction):
        if direction == "H":
            if col + ship_length > GRID_SIZE:
                return False
            return all(grid[row][col + i] == "~" for i in range(ship_length))
        else:
            if row + ship_length > GRID_SIZE:
                return False
            return all(grid[row + i][col] == "~" for i in range(ship_length))

    def place_ship(self, grid, ship_length, row, col, direction):
        if direction == "H":
            for i in range(ship_length):
                grid[row][col + i] = "S"
        else:
            for i in range(ship_length):
                grid[row + i][col] = "S"

    def place_all_ships(self, grid, ships):
        for ship, length in ships.items():
            placed = False
            while not placed:
                direction = random.choice(["H", "V"])
                row = random.randint(0, GRID_SIZE - 1)
                col = random.randint(0, GRID_SIZE - 1)
                if self.can_place_ship(grid, length, row, col, direction):
                    self.place_ship(grid, length, row, col, direction)
                    placed = True

    def check_hit(self, grid, row, col):
        if grid[row][col] == "S":
            grid[row][col] = "X"
            return True
        elif grid[row][col] == "~":
            grid[row][col] = "O"
            return False
        return None

    def show_instructions(self):
        instruction_window = tk.Toplevel(self.root)
        instruction_window.title("Инструкция к игре")
        instruction_window.geometry("400x300")
        
        instructions = (
            "Инструкция к игре 'Морской бой':\n\n"
            "1. Разместите свои корабли на сетке, кликнув по клеткам.\n"
            "2. Переключайте направление корабля правым кликом мыши.\n"
            "3. Начните игру, когда все корабли будут размещены.\n"
            "4. Кликайте по клеткам сетки противника, чтобы атаковать.\n"
            "5. Ваша цель - потопить все корабли противника.\n\n"
            "Удачи!"
        )
        
        tk.Label(instruction_window, text=instructions, justify="left", padx=10, pady=10).pack(expand=True)
        
        def on_close():
            instruction_window.destroy()
            self.choose_level()
        
        button = tk.Button(instruction_window, text="Понятно", command=on_close)
        button.pack(pady=10)
        
        instruction_window.grab_set()
        self.root.wait_window(instruction_window)

    def choose_level(self):
        level = simpledialog.askstring("Выбор уровня", "Введите уровень сложности (легкий, средний, сложный):")
        print(f"Выбран уровень сложности: {level}")
        self.show_main_window()

    def update_grid(self, grid, row_offset=0, col_offset=0, hide_ships=False):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                cell_value = grid[row][col]
                if hide_ships and cell_value == "S":
                    cell_value = "~"
                color = "blue" if cell_value == "~" else ("red" if cell_value == "X" else "white" if cell_value == "O" else "gray")
                cell = tk.Label(self.root, text=cell_value, width=2, height=1, bg=color, fg="black")
                cell.grid(row=row + 1 + row_offset, column=col + 1 + col_offset, padx=2, pady=2)
                if self.game_active:
                    if row_offset > 0:
                        cell.bind("<Button-1>", lambda e, r=row, c=col: self.on_attack_click(r, c))
                else:
                    cell.bind("<Button-1>", lambda e, r=row, c=col: self.on_cell_click(r, c))
                    cell.bind("<Button-3>", lambda e: self.on_right_click())

    def display_grid(self, grid, row_offset=0, col_offset=0, hide_ships=False):
        for i in range(GRID_SIZE):
            tk.Label(self.root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=0 + col_offset, padx=2, pady=2)
            tk.Label(self.root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=GRID_SIZE + 1 + col_offset, padx=2, pady=2)
            tk.Label(self.root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=0 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)
            tk.Label(self.root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=GRID_SIZE + 1 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)

        self.update_grid(grid, row_offset, col_offset, hide_ships)

    def on_cell_click(self, row, col):
        if self.ship_index < len(self.ship_lengths):
            ship_length = self.ship_lengths[self.ship_index]
            ship_name = self.ship_names[self.ship_index]
            if self.can_place_ship(self.grid_player, ship_length, row, col, self.selected_direction):
                self.place_ship(self.grid_player, ship_length, row, col, self.selected_direction)
                self.update_grid(self.grid_player)
                self.update_ship_info_label(ship_name, True)
                self.ship_index += 1
            else:
                print("Невозможно разместить корабль в этой позиции. Попробуйте снова.")
        if self.ship_index == len(self.ship_lengths):
            print("Все корабли размещены.")
            self.game_active = True
            self.display_grid(self.grid_player)
            self.display_grid(self.grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
            self.game_loop()

    def on_attack_click(self, row, col):
        if self.game_active:
            hit = self.check_hit(self.grid_computer, row, col)
            self.update_grid(self.grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
            if hit:
                print("Попадание!")
            else:
                print("Промах!")
            if all(cell != "S" for row in self.grid_computer for cell in row):
                print("Игрок выиграл!")
                self.game_active = False
                return
            self.root.after(75, self.computer_turn)
            if all(cell != "S" for row in self.grid_player for cell in row):
                print("Компьютер выиграл!")
                self.game_active = False

    def on_right_click(self):
        self.selected_direction = "V" if self.selected_direction == "H" else "H"
        print(f"Направление изменено на {self.selected_direction}")

    def computer_turn(self):
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            hit = self.check_hit(self.grid_player, row, col)
            if hit is not None:
                self.update_grid(self.grid_player, row_offset=0)
                break

    def game_loop(self):
        print("Ход игрока")

    def show_ships_info(self):
        for ship in self.ship_names:
            label = tk.Label(self.ship_info_frame, text=f"{ship}: {ships[ship]} клеток", width=20, height=2, anchor="w", bg="white", fg="black")
            label.pack(padx=5, pady=5)
            self.ship_labels[ship] = label

    def update_ship_info_label(self, ship_name, placed):
        if placed:
            self.ship_labels[ship_name].config(bg="lightgreen", fg="black")

    def show_main_window(self):
        self.root.deiconify()
        self.ship_info_frame = tk.Frame(self.root, width=200, height=300, bg="white", relief="sunken", bd=1)
        self.ship_info_frame.grid(row=0, column=GRID_SIZE + 2, rowspan=GRID_SIZE + 2, padx=10, pady=10)
        self.show_ships_info()
        self.display_grid(self.grid_player)
        self.place_all_ships(self.grid_computer, ships)
        self.display_grid(self.grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Морской бой")
    game = BattleshipGame(root)
    root.mainloop()
