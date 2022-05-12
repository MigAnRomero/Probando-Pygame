import sys

import pygame

def verificar_eventos():
    """Responde a las pulsaciones de teclas y los eventos del ratón"""
    # Escuchar eventos de teclado o de ratón
    # El bucle gestiona los eventos y código que actualiza la pantalla
    # Evento: acción que realiza un usuario mientras juega.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""
    # Volver a dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_configuraciones.bgcolor)
    nave.blitme()
        
    # Hacer visible la pantalla dibujada más reciente
    pygame.display.flip()