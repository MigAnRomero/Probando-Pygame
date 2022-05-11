import pygame

class Nave():
    """Sirve para gestionar el comportamiento de la nave"""

    def __init__(self, pantalla):
        """Inicializa la nave y establece su posición de partida"""
        
        self.pantalla = pantalla

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("Primer Juego/img/nave_uno.bmp") # Debo colocar toda la dirección completa para que funcione?
        self.rect = self.image.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom

    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.pantalla.blit(self.image, self.rect)