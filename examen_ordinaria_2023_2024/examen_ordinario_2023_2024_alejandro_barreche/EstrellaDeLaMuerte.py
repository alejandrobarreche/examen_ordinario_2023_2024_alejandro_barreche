from Planetas import PlanetaConcordia, PlanetaIlum, PlanetaKamino

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos_de_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_de_vida -= planeta.clasificacion
            print(f"La vida que le queda a la estrella de la muerte es: {self.puntos_de_vida}")
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}.")
            

def main():
    
    concordia = PlanetaConcordia()
    ilum = PlanetaIlum()
    kamino = PlanetaKamino()

    estrella_de_la_muerte = EstrellaDeLaMuerte()

    # Llamar al método destruir_planeta para cada planeta
    estrella_de_la_muerte.destruir_planeta(concordia)
    estrella_de_la_muerte.destruir_planeta(ilum)
    estrella_de_la_muerte.destruir_planeta(kamino)
    
if __name__ == "__main__":
    main()