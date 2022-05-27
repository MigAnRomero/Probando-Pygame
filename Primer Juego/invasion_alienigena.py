import pygame
# Cada elemento del videojuego es una superficie. Ej: los enemigos, el jugador, entre otros.
from pygame.sprite import Group
from configuraciones import Configuraciones
from estadisticas import Estadisticas
from marcador import Marcador
from button import Button
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
    
    # Crea el botón Play
    play_button = Button(ai_configuraciones, pantalla, "Play")
    
    
    # Crea una instancia para almacenar estadísticas del VJ y crea un marcador
    estadisticas = Estadisticas(ai_configuraciones)
    marcador = Marcador(ai_configuraciones, pantalla, estadisticas)

    # Crea una nave, un grupo de balas y un grupo de aliens
    nave = Nave(ai_configuraciones, pantalla)
    # Crea un grupo para almacenar las balas
    balas = Group()
    # Crea un grupo de aliens
    aliens = Group()
    
    # Crea la flota de alienógenas
    fj.crear_flota(ai_configuraciones, pantalla, nave, aliens)
    
    # Bucle de activación del videojuego:
    while True:
        # Escuchar eventos de teclado o de ratón
        fj.verificar_eventos(ai_configuraciones, pantalla, estadisticas, play_button, nave, aliens, balas)
        
        if estadisticas.game_active:
            nave.update() # La posición de la nave se actualiza en la pantalla usando las teclas
            fj.update_balas(ai_configuraciones, pantalla, estadisticas, 
                            marcador, nave, aliens, balas)
            # Actualizar la posición de cada alien
            fj.update_aliens(ai_configuraciones, estadisticas, pantalla, nave, aliens, balas)
        
        fj.actualizar_pantalla(ai_configuraciones, pantalla, estadisticas, 
                               marcador, nave, aliens, balas, play_button)

run_game() # Comienza el videojuego