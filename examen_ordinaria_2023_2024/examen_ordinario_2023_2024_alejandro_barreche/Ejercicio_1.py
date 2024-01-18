### PIRAMIDE ###

'''
Este código devuelve una pirámide de asteriscos formada por n niveles, 
en donde en cada nivel se aumenta en dos el número de asteriscos.
'''

# Pide al usuario un número y verifica que sea válido
'''
return: num (int) 
'''
def pedir_num():
    while True:
        num = input("Dime un número entero que sea mayor o igual a 1: ")
        try:
            num = int(num)
            if num >= 1:
                return num
            else:
                print("Ese número no vale")
        except ValueError:
            print("Por favor introduzca un número")



# Crea la pirámide de asteriscos
'''
parametro: num (int)
return: print()
'''
def crear_piramide(num):
    for i in range(1, num * 2, 2):
        espacio = (num * 2 - i) // 2
        print(" " * espacio + "*" * i)

if __name__ == "__main__":
    num = pedir_num()
    print(f"La pirámide de {num} niveles es:")
    crear_piramide(num)
        
