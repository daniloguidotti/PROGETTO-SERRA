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
