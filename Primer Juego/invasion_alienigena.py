import sys

import pygame
# Cada elemento del videojuego es una superficie. Ej: los enemigos, el jugador, entre otros.

from configuraciones import Configuraciones

def run_game():
    # Inicializar el juego, las configuraciones y crear un objeto pantalla
    pygame.init()
    ai_configuraciones = Configuraciones() # Se crea una instancia de configuraciones
    # Se crea una pantalla de visualizacion llamada "pantalla"
    pantalla = pygame.display.set_mode(
        (ai_configuraciones.screen_width, ai_configuraciones.screen_height))
    # Se digita el nombre del videojuego:
    pygame.display.set_caption("Invasión alienígena")

    # Bucle de activación del videojuego:
    while True:
        # Escuchar eventos de teclado o de ratón
        # El bucle gestiona los eventos y código que actualiza la pantalla
        # Evento: acción que realiza un usuario mientras juega.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Volver a dibujar la pantalla durante cada pasada por el bucle
        pantalla.fill(ai_configuraciones.bgcolor)
        # Hacer visible la pantalla dibujada más reciente
        pygame.display.flip()

run_game() # Comienza el videojuego