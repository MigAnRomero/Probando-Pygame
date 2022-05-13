class Configuraciones(object):
    """Sirve para almacenar todas las congiguraciones de Invasión Alienígena"""

    def __init__(self):
        """Inicializa las configuraciones del juego"""
        self.screen_width = 800
        self.screen_height = 600
        self.bgcolor = (230, 230, 230)
        
        # Configuraciones de la nave
        self.factor_velocidad_nave = 1.5