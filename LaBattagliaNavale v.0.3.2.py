import tkinter as tk
from tkinter import simpledialog
import random

# Dimensioni della griglia
GRID_SIZE = 10

# Definizione delle navi e delle loro lunghezze
ships = {
    "Portaerei": 5,
    "Corazzata": 4,
    "Incrociatore": 3,
    "Sommergibile": 3,
    "Cacciatorpediniere": 2
}

# Variabili globali per la gestione del posizionamento e dell'attacco
selected_ship = None
selected_direction = "H"
ship_lengths = list(ships.values())
ship_names = list(ships.keys())
ship_index = 0
game_active = False

# Funzione per creare una griglia vuota
def create_empty_grid(size):
    return [["~" for _ in range(size)] for _ in range(size)]

# Funzione per verificare se è possibile posizionare una nave
def can_place_ship(grid, ship_length, row, col, direction):
    if direction == "H":  # orizzontale
        if col + ship_length > GRID_SIZE:
            return False
        return all(grid[row][col + i] == "~" for i in range(ship_length))
    else:  # verticale
        if row + ship_length > GRID_SIZE:
            return False
        return all(grid[row + i][col] == "~" for i in range(ship_length))

# Funzione per posizionare una nave sulla griglia
def place_ship(grid, ship_length, row, col, direction):
    if direction == "H":
        for i in range(ship_length):
            grid[row][col + i] = "S"
    else:
        for i in range(ship_length):
            grid[row + i][col] = "S"

# Funzione per posizionare tutte le navi
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

# Funzione per verificare un colpo
def check_hit(grid, row, col):
    if grid[row][col] == "S":
        grid[row][col] = "X"  # Colpito
        return True
    elif grid[row][col] == "~":
        grid[row][col] = "O"  # Mancato
        return False
    return None  # Già colpito

def show_instructions():
    instruction_window = tk.Toplevel(root)
    instruction_window.title("Istruzioni del gioco")
    instruction_window.geometry("400x300")
    
    instructions = (
        "Istruzioni per il gioco 'Battaglia Navale':\n\n"
        "1. Posiziona le tue navi sulla griglia cliccando sulle celle.\n"
        "2. Cambia la direzione della nave cliccando con il tasto destro del mouse.\n"
        "3. Inizia il gioco quando tutte le navi sono state posizionate.\n"
        "4. Clicca sulle celle della griglia del nemico per attaccare.\n"
        "5. Il tuo obiettivo è affondare tutte le navi del nemico.\n\n"
        "Buona fortuna!"
    )
    
    tk.Label(instruction_window, text=instructions, justify="left", padx=10, pady=10).pack(expand=True)
    
    def on_close():
        instruction_window.destroy()
        choose_level()  # Passa alla selezione del livello
    
    button = tk.Button(instruction_window, text="Capito", command=on_close)
    button.pack(pady=10)

    # Attesa della chiusura della finestra delle istruzioni
    instruction_window.grab_set()
    root.wait_window(instruction_window)

# Funzione per scegliere il livello di difficoltà
def choose_level():
    level = simpledialog.askstring("Scelta del livello", "Inserisci il livello di difficoltà (facile, medio, difficile):")
    print(f"Livello di difficoltà scelto: {level}")
    show_main_window()

# Funzione per aggiornare la griglia
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
                if row_offset > 0:  # Attacco alla griglia del computer
                    cell.bind("<Button-1>", lambda e, r=row, c=col: on_attack_click(r, c))
            else:
                cell.bind("<Button-1>", lambda e, r=row, c=col: on_cell_click(r, c))
                cell.bind("<Button-3>", lambda e: on_right_click())

# Funzione per visualizzare la griglia
def display_grid(grid, row_offset=0, col_offset=0, hide_ships=False):
    for i in range(GRID_SIZE):
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=0 + col_offset, padx=2, pady=2)
        tk.Label(root, text=str(i + 1), width=2, height=1, bg="white", fg="black").grid(row=i + 1 + row_offset, column=GRID_SIZE + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=0 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)
        tk.Label(root, text=chr(65 + i), width=2, height=1, bg="white", fg="black").grid(row=GRID_SIZE + 1 + row_offset, column=i + 1 + col_offset, padx=2, pady=2)

    update_grid(grid, row_offset, col_offset, hide_ships)

# Gestore del clic sulla cella per posizionare le navi
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
            print("Impossibile posizionare la nave in questa posizione. Riprova.")
    if ship_index == len(ship_lengths):
        print("Tutte le navi sono state posizionate.")
        game_active = True
        display_grid(grid_player)
        display_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
        game_loop()

# Gestore del clic per l'attacco
def on_attack_click(row, col):
    global game_active
    if game_active:
        hit = check_hit(grid_computer, row, col)
        update_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)
        if hit:
            print("Colpito!")
        else:
            print("Mancato!")
        if all(cell != "S" for row in grid_computer for cell in row):
            print("Il giocatore ha vinto!")
            game_active = False
            return
        root.after(75, computer_turn)  # Ritardo prima del turno del computer
        if all(cell != "S" for row in grid_player for cell in row):
            print("Il computer ha vinto!")
            game_active = False

# Gestore del clic destro per cambiare direzione
def on_right_click():
    global selected_direction
    selected_direction = "V" if selected_direction == "H" else "H"
    print(f"Direzione cambiata in {selected_direction}")

# Funzione per eseguire il turno del computer
def computer_turn():
    while True:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        hit = check_hit(grid_player, row, col)
        if hit is not None:
            update_grid(grid_player, row_offset=0)
            break

# Ciclo di gioco principale
def game_loop():
    print("Turno del giocatore")

# Funzione per visualizzare le informazioni sulle navi
def show_ships_info():
    for ship in ship_names:
        label = tk.Label(ship_info_frame, text=f"{ship}: {ships[ship]} celle", width=20, height=2, anchor="w", bg="white", fg="black")
        label.pack(padx=5, pady=5)
        ship_labels[ship] = label

# Funzione per aggiornare le informazioni sulle navi
def update_ship_info_label(ship_name, placed):
    if placed:
        ship_labels[ship_name].config(bg="lightgreen", fg="black")

# Funzione per visualizzare la finestra principale del gioco
def show_main_window():
    global ship_info_frame, ship_labels
    root.deiconify()  # Mostra la finestra principale
    # Widget per visualizzare le informazioni sulle navi
    ship_info_frame = tk.Frame(root, width=200, height=300, bg="white", relief="sunken", bd=1)
    ship_info_frame.grid(row=0, column=GRID_SIZE + 2, rowspan=GRID_SIZE + 2, padx=10, pady=10)
    ship_labels = {}

    # Visualizza le informazioni sulle navi
    show_ships_info()

    # Visualizza la griglia vuota iniziale del giocatore
    display_grid(grid_player)

    # Posiziona le navi del computer
    place_all_ships(grid_computer, ships)

    # Visualizza la griglia del computer
    display_grid(grid_computer, row_offset=GRID_SIZE + 2, hide_ships=True)

# Crea una griglia vuota
grid_player = create_empty_grid(GRID_SIZE)
grid_computer = create_empty_grid(GRID_SIZE)

# Crea la finestra Tkinter
root = tk.Tk()
root.title("Battaglia Navale")
root.withdraw()  # Nascondi la finestra principale

# Mostra le istruzioni prima di iniziare il gioco
show_instructions()

# Avvia la finestra principale
root.mainloop()
