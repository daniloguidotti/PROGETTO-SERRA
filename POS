import tkinter as tk
import random

# Размеры сетки
GRID_SIZE = 10

# Определение кораблей и их длины
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2
}

# Функция для создания пустой сетки
def create_empty_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]

# Функция для проверки, можно ли разместить корабль
def can_place_ship(grid, ship_length, row, col, direction):
    if direction == "H":  # горизонтально
        if col + ship_length > GRID_SIZE:
            return False
        return all(grid[row][col + i] == "~" for i in range(ship_length))
    else:  # вертикально
        if row + ship_length > GRID_SIZE:
            return False
        return all(grid[row + i][col] == "~" for i in range(ship_length))

# Функция для размещения корабля на сетке
def place_ship(grid, ship_length, row, col, direction):
    if direction == "H":
        for i in range(ship_length):
            grid[row][col + i] = "S"
    else:
        for i in range(ship_length):
            grid[row + i][col] = "S"

# Функция для размещения всех кораблей
def place_all_ships(grid, ships):
    for ship, length in ships.items():
        placed = False
        while not placed:
            direction = random.choice(["H", "V"])
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if can_place_ship(grid, length, row, col, direction):
                place_ship(grid, length, row, col, direction)
                placed = True

# Создаем окно Tkinter
root = tk.Tk()
root.title("Морской бой")

# Создаем пустую сетку
grid_player = create_empty_grid(GRID_SIZE)
grid_computer = create_empty_grid(GRID_SIZE)

# Функция для отображения сетки
def display_grid(grid, row_offset=0, col_offset=0):
    for i in range(GRID_SIZE):
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=0 + col_offset, padx=2, pady=2)
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=GRID_SIZE + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=0 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=GRID_SIZE + 1 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            color = "blue" if cell_value == "~" else "gray"
            cell = tk.Label(root, text=cell_value, width=2, height=1, bg=color, fg="white")
            cell.grid(row=row + 1 + row_offset, column=col + 1 + col_offset, padx=2, pady=2)

# Функция для обновления сетки
def update_grid(grid, row_offset=0, col_offset=0):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            color = "blue" if cell_value == "~" else "gray"
            cell = tk.Label(root, text=cell_value, width=2, height=1, bg=color, fg="white")
            cell.grid(row=row + 1 + row_offset, column=col + 1 + col_offset, padx=2, pady=2)
    root.update()

# Функция для размещения кораблей игроком
def place_ships_manually(grid, ships):
    display_grid(grid)
    for ship, length in ships.items():
        placed = False
        while not placed:
            pos = input(f"Размещение {ship} (длина {length}). Введите координаты начальной позиции (например, A5): ").upper()
            direction = input("Введите направление (H для горизонтального, V для вертикального): ").upper()
            
            if len(pos) < 2 or direction not in ["H", "V"]:
                print("Неправильный ввод. Попробуйте снова.")
                continue

            row = ord(pos[0]) - 65
            try:
                col = int(pos[1:]) - 1
            except ValueError:
                print("Неправильный ввод. Попробуйте снова.")
                continue

            if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and can_place_ship(grid, length, row, col, direction):
                place_ship(grid, length, row, col, direction)
                update_grid(grid)
                placed = True
            else:
                print("Невозможно разместить корабль в этой позиции. Попробуйте снова.")

# Отображаем начальную пустую сетку игрока
display_grid(grid_player)

# Размещаем корабли игрока
print("Разместите свои корабли:")
place_ships_manually(grid_player, ships)

# Размещаем корабли компьютера
place_all_ships(grid_computer, ships)

# Отображаем сетку игрока и компьютера
display_grid(grid_player, row_offset=0, col_offset=0)
display_grid(grid_computer, row_offset=GRID_SIZE + 2, col_offset=0)

# Запускаем главное окно
root.mainloop()
