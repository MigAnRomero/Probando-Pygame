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