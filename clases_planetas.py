#ESTRELLA DE LA MUERTE

class planeta():
    def __init__(self,nombre,volumen,clasificación):
        self.nombre=nombre
        self.volumen=volumen
        self.clasificación=clasificación
    
class planeta1(planeta):
    def __init__(self,nombre,volumen,clasificacion):
        super().__init__('Concordia','500Km3','1')
class planeta2(planeta):
    def __init__(self,nombre,volumen,clasificacion):
        super().__init__('Ilum','1200Km3','2')
class planeta3(planeta):
    def __init__(self,nombre,volumen,clasificacion):
        super().__init__('Concordia','500Km3','1')

    

     