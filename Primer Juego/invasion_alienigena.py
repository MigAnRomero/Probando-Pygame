import pygame
# Cada elemento del videojuego es una superficie. Ej: los enemigos, el jugador, entre otros.
from pygame.sprite import Group
from configuraciones import Configuraciones
from nave import Nave
import funciones_juego as fj

def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    ai_configuraciones = Configuraciones() # Se crea una instancia de configuraciones
    # Se crea una pantalla de visualizacion llamada "pantalla"
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    # Se digita el nombre del videojuego:
    pygame.display.set_caption("Invasión alienígena")

    # Crea una nave
    nave = Nave(ai_configuraciones, pantalla)
    # Crea un grupo para almacenar las balas
    balas = Group()
    # Deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
    
    # Bucle de activación del videojuego:
    while True:
        # Escuchar eventos de teclado o de ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, nave, balas)
        nave.update() # La posición de la nave se actualiza en la pantalla usando las teclas
        balas.update()
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave, balas)

run_game() # Comienza el videojuego