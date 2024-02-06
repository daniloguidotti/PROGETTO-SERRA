import random

def crea_tabellone():
    tabellone = []
    for _ in range(5):
        riga = ["O"] * 5
        tabellone.append(riga)
    return tabellone

def stampa_tabellone(tabellone):
    for riga in tabellone:
        print(" ".join(riga))

def posizione_nave(tabellone):
    riga_nave = random.randint(0, len(tabellone) - 1)
    colonna_nave = random.randint(0, len(tabellone[0]) - 1)
    return (riga_nave, colonna_nave)

def input_giocatore():
    while True:
        riga = input("Indica la riga (0-4): ")
        colonna = input("Indica la colonna (0-4): ")

        if riga.isdigit() and colonna.isdigit():
            riga = int(riga)
            colonna = int(colonna)
            if 0 <= riga <= 4 and 0 <= colonna <= 4:
                return (riga, colonna)
        print("Input non valido. Assicurati di inserire numeri tra 0 e 4.")

def gioca():
    print("Benvenuto nella Battaglia Navale!")
    tabellone = crea_tabellone()
    posizione_nave_riga, posizione_nave_colonna = posizione_nave(tabellone)
    numero_tentativi = 0

    while True:
        print("\nTentativo numero:", numero_tentativi + 1)
        stampa_tabellone(tabellone)
        riga_giocatore, colonna_giocatore = input_giocatore()

        if (riga_giocatore, colonna_giocatore) == (posizione_nave_riga, posizione_nave_colonna):
            print("Congratulazioni! Hai colpito la nave!")
            break
        else:
            if tabellone[riga_giocatore][colonna_giocatore] == "X":
                print("Hai già provato in questa posizione.")
            else:
                print("Acqua! Riprova.")
                tabellone[riga_giocatore][colonna_giocatore] = "X"
            numero_tentativi += 1

        if numero_tentativi >= 5:
            print("Hai esaurito tutti i tentativi. La nave era in posizione", posizione_nave_riga, ",", posizione_nave_colonna)
            break

gioca()
