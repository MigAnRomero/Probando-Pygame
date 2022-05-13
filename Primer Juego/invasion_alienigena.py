import pygame
# Cada elemento del videojuego es una superficie. Ej: los enemigos, el jugador, entre otros.

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
    nave = Nave(pantalla)

    # Bucle de activación del videojuego:
    while True:
        # Escuchar eventos de teclado o de ratón
        fj.verificar_eventos(nave)
        fj.actualizar_pantalla(ai_configuraciones, pantalla, nave)

run_game() # Comienza el videojuego