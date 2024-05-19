import tkinter as tk
from tkinter import simpledialog
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

# Глобальные переменные для управления размещением и атакой
selected_ship = None
selected_direction = "H"
ship_lengths = list(ships.values())
ship_names = list(ships.keys())
ship_index = 0
game_active = False

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

# Функция для проверки попадания
def check_hit(grid, row, col):
    if grid[row][col] == "S":
        grid[row][col] = "X"  # Попадание
        return True
    elif grid[row][col] == "~":
        grid[row][col] = "O"  # Промах
        return False
    return None  # Уже стреляли сюда

# Функция для обновления сетки
def update_grid(grid, row_offset=0, col_offset=0, hide_ships=False):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            if hide_ships and cell_value == "S":
                cell_value = "~"
            color = "blue" if cell_value == "~" else ("red" if cell_value == "X" else "white" if cell_value == "O" else "gray")
            cell = tk.Label(root, text=cell_value, width=2, height=1, bg=color, fg="black")
            cell.grid(row=row + 1 + row_offset, column=col + 1 + col_offset, padx=2, pady=2)
            if game_active:
                if row_offset > 0:  # Атака по сетке компьютера
                    cell.bind("<Button-1>", lambda e, r=row, c=col: on_attack_click(r, c))
            else:
                cell.bind("<Button-1>", lambda e, r=row, c=col: on_cell_click(r, c))
                cell.bind("<Button-3>", lambda e: on_right_click())

# Функция для отображения сетки
def display_grid(grid, row_offset=0, col_offset=0, hide_ships=False):
    for i in range(GRID_SIZE):
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=0 + col_offset, padx=2, pady=2)
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=GRID_SIZE + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=0 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=GRID_SIZE + 1 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)

    update_grid(grid, row_offset, col_offset, hide_ships)

# Обработчик клика на ячейку для размещения кораблей
def on_cell_click(row, col):
    global ship_index, ship_lengths, ship_names, selected_direction, game_active

    if ship_index < len(ship_lengths):
        ship_length = ship_lengths[ship_index]
        ship_name = ship_names[ship_index]
        if can_place_ship(grid_player, ship_length, row, col, selected_direction):
            place_ship(grid_player, ship_length, row, col, selected_direction)
            update_grid(grid_player)
            update_ship_info_label(ship_name, True)
            ship_index += 1
        else:
            print("Невозможно разместить корабль в этой позиции. Попробуйте снова.")
    if ship_index == len(ship_lengths):
        print("Все корабли размещены.")
        game_active = True
        display_grid(grid_player)
        display_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
        game_loop()

# Обработчик клика для атаки
def on_attack_click(row, col):
    global game_active
    if game_active:
        hit = check_hit(grid_computer, row, col)
        update_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
        if hit:
            print("Попадание!")
        else:
            print("Промах!")
        if all(cell != "S" for row in grid_computer for cell in row):
            print("Игрок выиграл!")
            game_active = False
            return
        root.after(75, computer_turn)  # Задержка перед ходом компьютера
        if all(cell != "S" for row in grid_player for cell in row):
            print("Компьютер выиграл!")
            game_active = False

# Обработчик правого клика для смены направления
def on_right_click():
    global selected_direction
    selected_direction = "V" if selected_direction == "H" else "H"
    print(f"Направление изменено на {selected_direction}")

# Функция для выполнения хода компьютера
def computer_turn():
    while True:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        hit = check_hit(grid_player, row, col)
        if hit is not None:
            update_grid(grid_player, row_offset=0)
            break

# Основной игровой цикл
def game_loop():
    print("Ход игрока")

# Функция для выбора уровня сложности
def choose_level():
    level = simpledialog.askstring("Выбор уровня", "Введите уровень сложности (легкий, средний, сложный):")
    return level

# Функция для отображения информации о кораблях
def show_ships_info():
    for ship in ship_names:
        label = tk.Label(ship_info_frame, text=f"{ship}: {ships[ship]} клеток", width=20, height=2, anchor="w", bg="white", fg="black")
        label.pack(padx=5, pady=5)
        ship_labels[ship] = label

# Функция для обновления информации о кораблях
def update_ship_info_label(ship_name, placed):
    if placed:
        ship_labels[ship_name].config(bg="lightgreen", fg="black")

# Создаем пустую сетку
grid_player = create_empty_grid(GRID_SIZE)
grid_computer = create_empty_grid(GRID_SIZE)

# Создаем окно Tkinter
root = tk.Tk()
root.title("Морской бой")

# Виджет для отображения информации о кораблях
ship_info_frame = tk.Frame(root, width=200, height=300, bg="white", relief="sunken", bd=1)
ship_info_frame.grid(row=0, column=GRID_SIZE + 2, rowspan=GRID_SIZE + 2, padx=10, pady=10)
ship_labels = {}

# Запрашиваем уровень сложности у игрока
level = choose_level()
print(f"Выбран уровень сложности: {level}")

# Отображаем информацию о кораблях
show_ships_info()

# Отображаем начальную пустую сетку игрока
display_grid(grid_player)

# Размещаем корабликомпьютера
place_all_ships(grid_computer, ships)

# Отображаем сетку компьютера
display_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)

# Запускаем главное окно
root.mainloop()
