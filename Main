import pygame
import sys
import WebServer
import WebClient


pygame.init()

# Настройки окна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("La Battaglia Navale")

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Закраска фона

    pygame.display.flip()  # Обновление экрана


pygame.quit()
sys.exit()
