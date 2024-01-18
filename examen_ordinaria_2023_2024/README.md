# EXAMEN ORDINARIA 23/24
## Realizado por: Alejandro Barreche Ruiz

**Crear una Pirámide de Asteriscos**
- Escribe un programa que solicite un número entero n.
- Genera una pirámide de asteriscos con n niveles, comenzando con 1 asterisco y aumentando en 2 asteriscos por nivel.
- Valida que el número ingresado sea mayor o igual a 1.

**Estrella de la Muerte vs. Planetas**
- Crea clases de objetos tipo planeta utilizando herencia y un enumerado para asignar clasificación.
- Clase base Planeta con atributos nombre, volumen, y clasificacion.
- Tres subclases de Planeta: Concordia, Ilum, y Kamino.
- Crea una clase EstrellaDeLaMuerte con atributo de puntos de vida.
- Método destruir_planeta en EstrellaDeLaMuerte para destruir planetas según su clasificación.
- Crea instancias de planetas y la Estrella de la Muerte, llamando al método destruir_planeta.

**Naves Aliadas vs. Estrella de la Muerte**
- Crea dos subclases en un archivo Naves.py: NavePequena y NaveGrande, heredando de EstrellaDeLaMuerte.
- En EstrellaDeLaMuerte.py, modifica la clase para interactuar con las naves aliadas.
- Añade métodos para atacar naves aliadas y verificar si pueden ser destruidas.
- En main.py, crea instancias y llama a los métodos correspondientes.

**Contador de Tiempo para Partida de Ajedrez Blitz**
- Crea un programa que simula una partida de ajedrez blitz entre Magnus Carlsen y Hikaru Nakamura.
- Define variables de tiempo y establece un tiempo inicial de 10 segundos por movimiento.
- Inicia el juego con el turno de Magnus Carlsen.
- Solicita movimientos y valida el jugador en turno.
- Reduce el tiempo según el tiempo de movimiento y cambia el turno.
- Ajusta el tiempo de movimiento a 5 segundos cuando alcanzan 1 minuto.
- Finaliza el juego cuando se alcanza 0 segundos o el usuario ingresa "Salir".
- Muestra el resultado al final del juego.
