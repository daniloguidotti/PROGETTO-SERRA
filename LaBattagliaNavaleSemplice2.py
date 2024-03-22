def stampa_griglia(griglia):
    for riga in griglia:
        print(" ".join(riga))

def posiziona_navi(griglia):
    # Implementazione della disposizione casuale delle navi

def colpo_utente(griglia, riga, colonna):
    # Implementazione per verificare se il colpo ha colpito o mancato una nave

# Codice principale
griglia = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O']
]

posiziona_navi(griglia)

while True:
    stampa_griglia(griglia)
    riga = int(input("Inserisci il numero della riga: "))
    colonna = int(input("Inserisci il numero della colonna: "))
    colpo_utente(griglia, riga, colonna)
    # Implementa la logica per verificare se tutte le navi sono state affondate
