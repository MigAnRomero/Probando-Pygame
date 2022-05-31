class Configuraciones(object): # Voy a quitar "object" dentro del ()
    """Sirve para almacenar todas las congiguraciones de Invasión Alienígena"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 990
        self.screen_height = 690
        self.bg_color = (230, 230, 230)
        
        # Configuraciones de la nave
        self.cantidad_naves = 3 # Cantidad de vidas para el jugador
        
        # Configuraciones de balas
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60 # Color en RGB
        self.balas_allowed = 3
        
        # Configuraciones de Alien
        self.fleet_drop_speed = 10
        # Qué tan rápido se acelera el VJ
        self.escala_aceleracion = 1.1
        # Qué tan rápido aumentan los valores de puntos por aliens
        self.escala_puntaje = 1.5
        
        self.inicializa_configuraciones_dinamicas()
        
    def inicializa_configuraciones_dinamicas(self):
        """Inicializa la configuración que cambia a lo largo del videojuego"""
        self.factor_velocidad_nave = 1.5
        self.bala_factor_velocidad = 3
        self.alien_speed_factor = 1
        # fleet_direction, si es 1 representa a la derecha;
        # si es -1 representa a la derecha
        self.fleet_direction = 1
        # Puntuación
        self.puntos_alien = 50
        
    def aumentar_velocidad(self):
        """Aumenta la configuración de velocidad y los valores de puntos por aliens"""
        self.factor_velocidad_nave *= self.escala_aceleracion
        self.bala_factor_velocidad *= self.escala_aceleracion
        self.alien_speed_factor *= self.escala_aceleracion
        
        self.puntos_alien = int(self.puntos_alien * self.escala_puntaje)
        print(self.puntos_alien)