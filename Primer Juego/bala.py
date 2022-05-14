import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    """Sirve para manejar las balas disparadas desde la nave"""
    def __init__(self, ai_configuraciones, pantalla, nave):
        super (Bala, self).__init__()
        self.pantalla = pantalla
        
        # Crea un bala rect en (0, 0) y luego establece la posición correcta
        self.rect = pygame.Rect(0, 0, ai_configuraciones.bala_width,
                                ai_configuraciones.bala_height)
        # La bala sale disparada desde la ubicación actual de la nave
        self.rect.centerx = nave.rect.centerx
        # La bala emerge en la parte superior de la nave
        self.rect.top = nave.rect.top
        
        # Almacena la posición de la bala como un valor decimal
        self.y = float(self.rect.y)
        # Se almacena el color de la bala digitado en "configuraciones.py"
        self.color = ai_configuraciones.bala_color
        # Se almacena la velocidad de la bala digitado en "configuraciones.py"
        self.factor_velocidad = ai_configuraciones.bala_velocidad
        
    # El método update gestiona la posición de la bala
    # porque, cuando la bala se dispara, se mueve hacia arriba en la pantalla,
    # ocasionando una disminución del valor de la coordenada "y"
    def update(self):
        """Mueve la bala hacia arriba en la pantalla"""
        # Actualiza la posición decimal de la bala
        self.y -= self.factor_velocidad
        # Actualiza la posición del rect
        self.rect.y = self.y
        
    def draw_bala(self):
        """Dibuja la bala en la pantalla"""
        pygame.draw.rect(self.pantalla, self.color, self.rect)