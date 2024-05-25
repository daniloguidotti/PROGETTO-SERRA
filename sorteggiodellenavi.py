import tkinter as tk

def show_draw_animation(root):
    # Creazione della finestra di dialogo per il sorteggio
    draw_window = tk.Toplevel(root)
    draw_window.title("Sorteggio")
    draw_window.geometry("300x200")
    
    # Etichetta iniziale
    label = tk.Label(draw_window, text="Sorteggio in corso...", font=("Arial", 16))
    label.pack(expand=True)

    # Simula un'animazione di sorteggio cambiando il testo dopo 2 secondi e chiudendo la finestra dopo 4 secondi
    root.after(2000, lambda: label.config(text="Il giocatore X inizia per primo!"))
    root.after(4000, lambda: draw_window.destroy())
    
    # Imposta la finestra di sorteggio come modale
    draw_window.grab_set()
    root.wait_window(draw_window)

# Crea la finestra principale Tkinter
root = tk.Tk()
root.title("Battaglia Navale")

# Aggiungi un pulsante per mostrare l'animazione del sorteggio
button = tk.Button(root, text="Mostra Sorteggio", command=lambda: show_draw_animation(root))
button.pack(pady=20)

# Avvia il ciclo principale di Tkinter
root.mainloop()

