

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_naves_aliadas(self, nave_aliada):
        if nave_aliada.puntos_de_vida <= self.puntos_de_vida:
            print(f"La Estrella de la Muerte ha destruido la nave aliada {nave_aliada.nombre}, la cual tenía una vida de {nave_aliada.puntos_de_vida}.")
            self.puntos_de_vida -= nave_aliada.puntos_de_vida
            print(f"La vida que le queda a la estrella de la muerte es: {self.puntos_de_vida}")
            print()
        else:
            print(f"No se puede destruir la nave aliada {nave_aliada.nombre}, la cual tenía una vida de {nave_aliada.puntos_de_vida}.")
            print()
            
class NavePequeña(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos_de_vida):
        super().__init__()
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
        
class NaveGrande(EstrellaDeLaMuerte):
    def __init__(self, nombre, puntos_de_vida):
        super().__init__()
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
            