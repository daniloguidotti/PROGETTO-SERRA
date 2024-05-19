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

# Создаем пустую сетку
grid = create_empty_grid(GRID_SIZE)

# Размещаем все корабли
place_all_ships(grid, ships)

# Создаем окно Tkinter
root = tk.Tk()
root.title("Морской бой")

# Функция для отображения сетки
def display_grid(grid):
    # Добавление меток для строк и столбцов с обеих сторон
    for i in range(GRID_SIZE):
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1, column=0, padx=2, pady=2)
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1, column=GRID_SIZE + 1, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=0, column=i + 1, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=GRID_SIZE + 1, column=i + 1, padx=2, pady=2)

    # Отображение сетки с кораблями
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            color = "blue" if cell_value == "~" else "gray"
            cell = tk.Label(root, text=cell_value, width=2, height=1, bg=color, fg="white")
            cell.grid(row=row + 1, column=col + 1, padx=2, pady=2)

# Отображаем сетку
display_grid(grid)

# Запускаем главное окно
root.mainloop()
