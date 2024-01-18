from enum import Enum

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion
    

class ClasificacionPlaneta(Enum):
    Concordia = 1
    Ilum = 2
    Kamino = 3

class PlanetaConcordia(Planeta):
    def __init__(self, nombre="Concordia", volumen=500, clasificacion=ClasificacionPlaneta.Concordia.value):
        super().__init__(nombre, volumen, clasificacion)

class PlanetaIlum(Planeta):
    def __init__(self, nombre="Ilum", volumen=1200, clasificacion=ClasificacionPlaneta.Ilum.value):
        super().__init__(nombre, volumen, clasificacion)

class PlanetaKamino(Planeta):
    def __init__(self, nombre="Kamino", volumen=800, clasificacion=ClasificacionPlaneta.Kamino.value):
        super().__init__(nombre, volumen, clasificacion)
