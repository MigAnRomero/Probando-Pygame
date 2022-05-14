import sys

import pygame

def verificar_eventos_keydown(event, nave):
    """Responde a las pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True

def verificar_eventos_keyup(event, nave):
    """Responde a las pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False
            
def verificar_eventos(nave):
    """Responde a las pulsaciones de teclas y los eventos del ratón"""
    # Escuchar eventos de teclado o de ratón
    # El bucle gestiona los eventos y código que actualiza la pantalla
    # Evento: acción que realiza un usuario mientras juega.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, nave)
            
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
            

def actualizar_pantalla(ai_configuraciones, pantalla, nave):
    """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""
    # Volver a dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_configuraciones.bgcolor)
    nave.blitme()
        
    # Hacer visible la pantalla dibujada más reciente
    pygame.display.flip()