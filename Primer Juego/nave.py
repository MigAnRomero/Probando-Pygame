import pygame

class Nave():
    """Sirve para gestionar el comportamiento de la nave"""

    def __init__(self, ai_configuraciones, pantalla):
        """Inicializa la nave y establece su posición de partida"""
        
        self.pantalla = pantalla
        self.ai_configuraciones = ai_configuraciones

        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("Primer Juego/img/nave_uno.bmp") # Debo colocar toda la dirección completa para que funcione?
        self.rect = self.image.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empieza cada nueva nave en la parte inferior central de la pantalla
        self.rect.centerx = self.pantalla_rect.centerx
        self.rect.bottom = self.pantalla_rect.bottom
        
        # Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centerx)
        
        # Banderas de movimiento
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Actualiza la posición de la nave según las banderas de movimiento"""
        # Movimiento a la derecha
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            #self.rect.centerx += 1
            self.center += self.ai_configuraciones.factor_velocidad_nave
        # Movimiento a la izquierda
        if self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.center -= self.ai_configuraciones.factor_velocidad_nave

        # Actualiza el objeto rect desde self.center
        self.rect.centerx = self.center
        
    def blitme(self):
        """Dibuja la nave en su ubicación actual"""
        self.pantalla.blit(self.image, self.rect)