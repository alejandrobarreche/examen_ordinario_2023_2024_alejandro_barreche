import time

tiempo_carlsen = 180
tiempo_nakamura = 180
tiempo_movimiento = 10

def realizar_movimiento(jugador, tiempo_movimiento):
    global tiempo_carlsen, tiempo_nakamura  # Declarar las variables como globales

    print(f"\nTurno de {jugador}")
    print(f"Tiempo actual - Carlsen: {tiempo_carlsen} segundos, Nakamura: {tiempo_nakamura} segundos")

    while True:
        movimiento = input(f"Ingrese el movimiento para {jugador} (Salir para terminar): ").lower()

        if movimiento == "salir":
            print("Partida terminada.")
            return True

        if movimiento == jugador.lower():
            tiempo_restante = tiempo_carlsen if jugador == "Carlsen" else tiempo_nakamura
            tiempo_restante -= tiempo_movimiento

            if tiempo_restante <= 0:
                print(f"\nTiempo agotado para {jugador}. ¡{jugador} pierde!")
                return True

            if tiempo_restante <= 60 and tiempo_movimiento == 10:
                tiempo_movimiento = 5

            if jugador == "Carlsen":
                tiempo_carlsen = tiempo_restante
            else:
                tiempo_nakamura = tiempo_restante

            return False
        else:
            print(f"Ingrese el movimiento correcto para {jugador}.")

while True:
    if realizar_movimiento("Carlsen", tiempo_movimiento):
        break

    if realizar_movimiento("Nakamura", tiempo_movimiento):
        break

# Mostrar resultado final
if tiempo_carlsen <= 0 and tiempo_nakamura <= 0:
    print("\n¡Partida empatada!")
elif tiempo_carlsen <= 0:
    print("\n¡Hikaru Nakamura gana!")
else:
    print("\n¡Magnus Carlsen gana!")
