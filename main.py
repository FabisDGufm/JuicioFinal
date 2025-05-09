import AVL
import primi

def main():
    print("""Bienvenido a "Juicio Final"
    1. Versión con AVL
    2. Versión con datos primitivos
""")
    try:
        modo = int(input("Ingresa la versión que deseas utilizar (1 o 2): "))
        if modo == 1:
            print("""
Activando modo AVL...
""")
            print("""                ⚖️ EL JUICIO FINAL ⚖️
Los dioses han asignado karmas aleatorios a cada grupo humano.
                  
Tú decidirás el destino de la humanidad.
Grupos generados:
""")
            AVL.insert()
            menuAVL()
        elif modo == 2:
            print("""
Activando modo Datos Primitivos...
""")
            print("""                ⚖️ EL JUICIO FINAL ⚖️
Los dioses han asignado karmas aleatorios a cada grupo humano.

Tú decidirás el destino de la humanidad.
Grupos generados:
""")
            primi.insert()
            menuPrimi()
        else:
            print("""
    Respuesta no válida, intenta de nuevo.
                  """)
            main()
    except ValueError:
        print("""
    Respuesta no válida, intenta de nuevo
                  """)
        main()

def menuAVL(): 
    print("""🧭 Menú de opciones:
    1. Ver al grupo más bondadoso
    2. Ver al grupo más malvado
    3. Ver todos los grupos ordenados por karma
    4. Ver grupos con karma entre [x] y [y]
    5. Emitir juicio
    6. Salir""")

    try:
        opc = int(input("Ingresa el número de la opción que deseas realizar: "))
        if (opc == 1):
            print()
        if (opc == 2):
            print()
        if (opc == 3):
            print()
        if (opc == 4):
            print()
        if (opc == 5):
            print("""
Tu decisión:
    1. Salvar al más bondadoso
    2. Eliminar al más malvado
    3. Salvar los del rango 10-80
    4. Dejar que el destino decida (random)""")
        if (opc == 6):
            print()
    except ValueError:
        print("Respuesta no válida, intenta de nuevo.")
        menuAVL()

def menuPrimi(): 
    print("""🧭 Menú de opciones:
    1. Ver al grupo más bondadoso
    2. Ver al grupo más malvado
    3. Ver todos los grupos ordenados por karma
    4. Ver grupos con karma entre [x] y [y]
    5. Emitir juicio
    6. Salir""")
    opc = input("Ingresa el número de la opción que deseas realizar: ")

    try:
        if (opc == 1):
            print()
        if (opc == 2):
            print()
        if (opc == 3):
            print()
        if (opc == 4):
            print()
        if (opc == 5):
            print("""
Tu decisión:
    1. Salvar al más bondadoso
    2. Eliminar al más malvado
    3. Salvar los del rango 10-80
    4. Dejar que el destino decida (random)""")
        if (opc == 6):
            print()
    except ValueError:
        print("Respuesta no válida, intenta de nuevo.")
        menuPrimi()

main()