from Naves import EstrellaDeLaMuerte, NaveGrande, NavePequeña

def main():
    nave1 = NavePequeña("Elon Musk", 450)
    nave2 = NaveGrande("Space X", 700)
    
    estrella_de_la_muerte = EstrellaDeLaMuerte()
    
    estrella_de_la_muerte.destruir_naves_aliadas(nave1)
    estrella_de_la_muerte.destruir_naves_aliadas(nave2)
    
main()
            

