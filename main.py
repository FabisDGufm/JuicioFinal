def main():
    print("""Bienvenido a "Juicio Final"
    1. Versión con AVL
    2. Versión con datos primitivos
""")
    try:
        modo = int(input("Ingresa la versión que deseas utilizar (1 o 2): "))
        if modo == 1:
            menuAVL()
        elif modo == 2:
            menuPrimi()
        else:
            
            print("""
    Respuesta no válida, intenta de nuevo.
                  """)
            main()
    except ValueError:
        print("Respuesta no válida, intenta de nuevo.")
        main()

def menuAVL(): 
    print("d")

def menuPrimi(): 
    print("a")

main()