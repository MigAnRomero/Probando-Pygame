class Estadisticas():
    """Seguimiento de las estadísticas de Invasión Alienígena"""
    def __init__(self, ai_configuraciones):
        """Inicializa las estadñisticas"""
        self.ai_configuraciones = ai_configuraciones
        self.reset_stats()
        
    def reset_stats(self):
        """Inicializa estadñisticas que pueden cambiar durante el juego"""
        self.naves_restantes = self.ai_configuraciones.cantidad_naves
        