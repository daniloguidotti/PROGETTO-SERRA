import tkinter as tk
import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.last_login = datetime.date.today()
    
    def win_battle(self):
        self.points += 3
    
    def lose_battle(self):
        self.points -= 1
    
    def daily_bonus(self):
        today = datetime.date.today()
        if today > self.last_login:
            self.points += 2
            self.last_login = today
    
    def __str__(self):
        return f"Giocatore: {self.name}, Punti: {self.points}"

class BattleshipGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Battaglia Navale - Sistema di Punteggio")
        
        self.player = Player("Giocatore 1")
        
        self.label = tk.Label(master, text=str(self.player))
        self.label.pack()
        
        self.win_button = tk.Button(master, text="Vittoria nella battaglia", command=self.win_battle)
        self.win_button.pack()
        
        self.lose_button = tk.Button(master, text="Sconfitta nella battaglia", command=self.lose_battle)
        self.lose_button.pack()
        
        self.bonus_button = tk.Button(master, text="Ricevi bonus giornaliero", command=self.daily_bonus)
        self.bonus_button.pack()
    
    def update_label(self):
        self.label.config(text=str(self.player))
    
    def win_battle(self):
        self.player.win_battle()
        self.update_label()
    
    def lose_battle(self):
        self.player.lose_battle()
        self.update_label()
    
    def daily_bonus(self):
        self.player.daily_bonus()
        self.update_label()

if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipGame(root)
    root.mainloop()
