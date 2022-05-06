import sys

import pygame
# Cada elemento del videojuego es una superficie. Ej: los enemigos, el jugador, entre otros.

def run_game():
    pygame.init()
    # Se crea una pantalla de visualizacion llamada "pantalla"
    # pixeles de ancho: 800; pixeles de alto: 600
    pantalla = pygame.display.set_mode((800, 600))
    # Se digita el nombre del videojuego:
    pygame.display.set_caption("Invasión alienígena")
    
    # Cambiar el color de fondo por defecto (negro) de la pantalla:
    bg_color = (230, 230, 230) # Se utiliza los colores RGB


    # Bucle de activación del videojuego:
    while True:
        # El bucle gestiona los eventos y código que actualiza la pantalla
        # Evento: acción que realiza un usuario mientas juega.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Volver a dibujar la pantalla durante cada pasada por el bucle
        pantalla.fill(bg_color)
        # Hacer visible la pantalla dibujada más reciente
        pygame.display.flip()

run_game() # Comienza el videojuego