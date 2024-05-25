import tkinter as tk
from tkinter import simpledialog

def show_instructions(root):
    # Crea una nuova finestra di dialogo per le istruzioni
    instruction_window = tk.Toplevel(root)
    instruction_window.title("Istruzioni del gioco")
    instruction_window.geometry("450x350")
    
    # Testo delle istruzioni
    instructions = (
        "Istruzioni per il gioco 'Battaglia Navale':\n\n"
        "1. Posiziona le tue navi sulla griglia cliccando sulle celle.\n"
        "2. Le navi possono essere posizionate orizzontalmente o verticalmente.\n"
        "3. Cambia la direzione della nave cliccando con il tasto destro del mouse.\n"
        "4. Le navi possono essere posizionate in prossimità, ma non possono sovrapporsi.\n"
        "5. Inizia il gioco quando tutte le navi sono state posizionate.\n"
        "6. Clicca sulle celle della griglia del nemico per attaccare.\n"
        "7. Se colpisci una nave, la cella verrà contrassegnata in rosso.\n"
        "8. Se manchi, la cella verrà contrassegnata in bianco.\n"
        "9. Il tuo obiettivo è affondare tutte le navi del nemico.\n\n"
        "Buona fortuna!"
    )
    
    # Aggiunge le istruzioni alla finestra
    tk.Label(instruction_window, text=instructions, justify="left", padx=10, pady=10).pack(expand=True)
    
    # Funzione chiamata quando il pulsante "Capito" viene premuto
    def on_close():
        instruction_window.destroy()
        choose_level(root)  # Passa alla selezione del livello
    
    # Aggiunge un pulsante "Capito" alla finestra delle istruzioni
    button = tk.Button(instruction_window, text="Capito", command=on_close)
    button.pack(pady=10)
    
    # Imposta la finestra delle istruzioni come modale
    instruction_window.grab_set()
    root.wait_window(instruction_window)

def choose_level(root):
    # Richiede all'utente di inserire il livello di difficoltà
    level = simpledialog.askstring("Scelta del livello", "Inserisci il livello di difficoltà (facile, medio, difficile):")
    if level:
        print(f"Livello di difficoltà scelto: {level}")
        start_game(root, level)  # Inizia il gioco con il livello scelto

def start_game(root, level):
    # Crea una nuova finestra di gioco
    game_window = tk.Toplevel(root)
    game_window.title("Battaglia Navale - Gioco")
    game_window.geometry("800x600")

    # Mostra il livello di difficoltà scelto
    tk.Label(game_window, text=f"Iniziando il gioco a livello: {level}", font=("Helvetica", 16)).pack(pady=20)
    # Aggiungi qui il resto della logica per avviare il gioco in base al livello scelto

    # Funzione chiamata quando la finestra di gioco viene chiusa
    def on_close():
        game_window.destroy()
        root.destroy()  # Chiude l'applicazione principale quando la finestra di gioco viene chiusa

    # Imposta il protocollo di chiusura della finestra
    game_window.protocol("WM_DELETE_WINDOW", on_close)

# Crea la finestra principale Tkinter
root = tk.Tk()
root.title("Battaglia Navale")
root.withdraw()  # Nasconde la finestra principale

# Mostra le istruzioni prima di iniziare il gioco
show_instructions(root)

# Avvia la finestra principale
root.mainloop()
