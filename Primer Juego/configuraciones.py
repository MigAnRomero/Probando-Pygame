class Configuraciones(object):
    """Sirve para almacenar todas las congiguraciones de Invasión Alienígena"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 800
        self.screen_height = 600
        self.bgcolor = (230, 230, 230)
        
        # Configuraciones de la nave
        self.factor_velocidad_nave = 1.5
        
        # Configuraciones de balas
        self.bala_factor_velocidad = 1
        self.bala_width = 3
        self.bala_height = 15
        self.bala_color = 60, 60, 60 # Color en RGB
        self.balas_allowed = 3
        
        # Configuraciones de Alien
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 1
        # fleet_direction, si es 1 representa a la derecha;
        # si es -1 representa a la derecha
        self.fleet_direction = 1