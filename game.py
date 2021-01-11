# Bibliotecas externas
import os  # Biblioteca para direcionamento do endereço dos arquivos.

import pygame  # Biblioteca para a janela do jogo e evento de mouse.
import pygame.freetype  # Sub biblioteca para a fonte.

# Meu código
from widgets import PushButton, Text, Border, Panel, Color, ToggleButton, Window



class Workplace:
    def __init__(self, image, title_panel, ):



# Classe do manager do Jogo.
class Game:
    def __init__(self, window):
        self.width = window.get_width()
        self.height = window.get_height()
        self.window = window

        self.running = True

    def run(self):
        timer = pygame.time.Clock()
        while self.running:
            self.event_handler()

            timer.tick(60)
            pygame.display.update()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Hi")

            if event.type == pygame.MOUSEBUTTONUP:
                print("Hello")

    def close_game(self):
        self.running = False


def quadrature(p, q):
    return (p[0]-q[0])**2+(p[1]-q[1])**2