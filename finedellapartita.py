import tkinter as tk
from tkinter import messagebox

def end_game(winner):
    # Mostra un messaggio di fine partita e chiede all'utente se vuole giocare di nuovo
    if winner == "player":
        play_again = messagebox.askyesno("Fine della partita", "Hai vinto! Vuoi giocare di nuovo?")
    else:
        play_again = messagebox.askyesno("Fine della partita", "Il computer ha vinto. Vuoi giocare di nuovo?")
    
    # Gestisce la risposta dell'utente
    if play_again:
        reset_game()
    else:
        root.quit()

def reset_game():
    # Funzione per resettare il gioco (da implementare)
    print("Gioco resettato.")
    # Aggiungi qui la logica per resettare il gioco

# Creazione della finestra principale Tkinter
root = tk.Tk()
root.title("Battaglia Navale")

# Pulsante per simulare la fine del gioco per il giocatore
player_win_button = tk.Button(root, text="Fine Gioco (Vittoria Giocatore)", command=lambda: end_game("player"))
player_win_button.pack(pady=10)

# Pulsante per simulare la fine del gioco per il computer
computer_win_button = tk.Button(root, text="Fine Gioco (Vittoria Computer)", command=lambda: end_game("computer"))
computer_win_button.pack(pady=10)

# Avvia il ciclo principale di Tkinter
root.mainloop()
