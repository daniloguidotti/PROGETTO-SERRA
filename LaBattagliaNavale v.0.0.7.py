def LaBattagliaNavale():
    class Nave:
        def __init__(self, name, photo_path, stato):
            self.name = name
            self.photo_path = photo_path
            self.stato = stato
        def display_info(self):
            print(f"Name: {self.name}")
            print(f"Stato: {self.stato}")
        def display_photo(self):
        # Здесь можно добавить код для отображения фотографии корабля
        # Например, использовать библиотеку PIL для загрузки и отображения изображения
            pass

    #scialuppa =
    NaveGrande = Nave("Littorio", "frigate.jpg")
    NaveMedia = Nave("Incrociatore", "frigate.jpg")
    NavePiccola = Nave("Cacciatorpediniere", "frigate.jpg")
    #Portaerei =
        
        
# Вывод информации о кораблях
NaveGrande.display_foto()
print()
NaveMedia.display_info()
print()
NavePiccola.display_info()
print()
