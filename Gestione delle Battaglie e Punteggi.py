def main():
    player = player("Giocatore 1")

    while True:
        print(player)
        print("1. Vittoria nella battaglia")
        print("2. Sconfitta nella battaglia")
        print("3. Ricevi bonus giornaliero")
        print("4. Esci")
        
        choice = input("Scegli un'opzione: ")
        
        if choice == '1':
            player.win_battle()
        elif choice == '2':
            player.lose_battle()
        elif choice == '3':
            player.daily_bonus()
        elif choice == '4':
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()


