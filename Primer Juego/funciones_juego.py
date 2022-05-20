import sys
import pygame
from bala import Bala
from alien import Alien

def verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas):
    """Responde a las pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = True
    elif event.key == pygame.K_LEFT:
        nave.moving_left = True
    elif event.key == pygame.K_SPACE:
        fuego_bala(ai_configuraciones, pantalla, nave, balas)
    elif event.key == pygame.K_q:
        sys.exit() # La tecla "Q" cierra la pantalla del videojuego

def verificar_eventos_keyup(event, nave):
    """Responde a las pulsaciones de teclas"""
    if event.key == pygame.K_RIGHT:
        nave.moving_right = False
    elif event.key == pygame.K_LEFT:
        nave.moving_left = False
            
def verificar_eventos(ai_configuraciones, pantalla, nave, balas):
    """Responde a las pulsaciones de teclas y los eventos del ratón"""
    # Escuchar eventos de teclado o de ratón
    # El bucle gestiona los eventos y código que actualiza la pantalla
    # Evento: acción que realiza un usuario mientras juega.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            verificar_eventos_keydown(event, ai_configuraciones, pantalla, nave, balas)
            
        elif event.type == pygame.KEYUP:
            verificar_eventos_keyup(event, nave)
            

def actualizar_pantalla(ai_configuraciones, pantalla, nave, aliens, balas):
    """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla"""
    # Volver a dibujar la pantalla durante cada pasada por el bucle
    pantalla.fill(ai_configuraciones.bgcolor)
    # Vuelve a dibujar todas las balas detrás de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)
        
    # Hacer visible la pantalla dibujada más reciente
    pygame.display.flip()
    
def update_balas(balas):
    """Actualiza la posición de las balas y elimina las antiguas"""
    # Actualiza las posiciones de las balas
    balas.update()
    # Deshace las balas que han desaparecido
    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)
            
def fuego_bala(ai_configuraciones, pantalla, nave, balas):
    """Dispara una bala si aún no ha alcanzado el límite"""
    # Crea una nueva bala y la agrega al grupo de balas
    if len(balas) < ai_configuraciones.balas_allowed:
        nueva_bala = Bala(ai_configuraciones, pantalla, nave)
        balas.add(nueva_bala)
        
def crear_flota(ai_configuraciones, pantalla, aliens):
    """Crea una flota completa de alienígenas"""
    # Crea un alien y encuentra el número de aliens seguidos
    # El espacio entre cada alien es igual a un ancho del alien
    alien = Alien(ai_configuraciones, pantalla)
    alien_width = alien.rect.width
    # Calcular el espacio horizontal disponible para los aliens
    available_space_x = ai_configuraciones.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    # Crea la primera fila de aliens
    for alien_number in range(number_aliens_x):
        # Crea un alien y lo coloca en la fila
        alien = Alien(ai_configuraciones, pantalla)
        # El alien se va creando hacia la derecha
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)