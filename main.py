import AVL
import primi

def main():
    print("""Bienvenido a "Juicio Final"
    1. Versión con AVL
    2. Versión con datos primitivos
    3. Salir
""")
    try:
        modo = int(input("Ingresa la versión que deseas utilizar (1, 2 o 3): "))
        if modo == 1:
            print("""\nActivando modo AVL...\n""")
            print("""                ⚖️ EL JUICIO FINAL ⚖️
Los dioses han asignado karmas aleatorios a cada grupo humano.
                  
Tú decidirás el destino de la humanidad.
Grupos generados:
""")
            AVL.insert()
            menuAVL()
        elif modo == 2:
            print("""\nActivando modo Datos Primitivos...\n""")
            print("""                ⚖️ EL JUICIO FINAL ⚖️
Los dioses han asignado karmas aleatorios a cada grupo humano.

Tú decidirás el destino de la humanidad.
Grupos generados:
""")
            primi.insert()
            menuPrimi()
        elif modo == 3:
            print("Saliendo del programa...")
        else:
            print("\nRespuesta no válida. Reinicia el programa.\n")
    except ValueError:
        print("\nRespuesta no válida. Reinicia el programa.\n")

def menuAVL(): 
    while True:
        print("""🧭 Menú de opciones:
    1. Ver al grupo más bondadoso
    2. Ver al grupo más malvado
    3. Ver todos los grupos ordenados por karma
    4. Ver grupos con karma entre 10 y 80
    5. Emitir juicio
    6. Salir""")

        try:
            opc = int(input("Ingresa el número de la opción que deseas realizar: "))
            if opc == 1:
                nom, karma = AVL.buscar_max()
                print(f"🟢 El grupo más bondadoso es: {nom} con karma {karma}")
            elif opc == 2:
                nom, karma = AVL.buscar_min()
                print(f"🔴 El grupo más malvado es: {nom} con karma {karma}")
            elif opc == 3:
                AVL.inorder()
                print()
            elif opc == 4:
                AVL.buscar_rango()
                print()
            elif opc == 5:
                print("""\nTu decisión:
    1. Salvar al más bondadoso
    2. Eliminar al más malvado
    3. Salvar los del rango 10-80
    4. Dejar que el destino decida (random)\n""")
                den = int(input("Ingresa el número de la opción que deseas realizar: "))
                AVL.decision(den)
                print("\n⚖️ El juicio ha sido emitido. Fin del Juicio Final.")
                exit()
            elif opc == 6:
                print("Saliendo del modo AVL...\n")
                exit()
            else:
                print("Opción no válida, intenta de nuevo.\n")
        except ValueError:
            print("Respuesta no válida, intenta de nuevo.\n")

def menuPrimi(): 
    while True:
        print("""🧭 Menú de opciones:
    1. Ver al grupo más bondadoso
    2. Ver al grupo más malvado
    3. Ver todos los grupos ordenados por karma
    4. Ver grupos con karma entre 10 y 80
    5. Emitir juicio
    6. Salir""")

        try:
            opc = int(input("Ingresa el número de la opción que deseas realizar: "))
            if opc == 1:
                nom, karma = primi.buscar_max()
                print(f"🟢 El grupo más bondadoso es: {nom} con karma {karma}")
                print()
            elif opc == 2:
                nom, karma = primi.buscar_min()
                print(f"🔴 El grupo más malvado es: {nom} con karma {karma}")
                print()
            elif opc == 3:
                primi.inorder()
                print()
            elif opc == 4:
                primi.buscar_rango()
                print()
            elif opc == 5:
                print("""\nTu decisión:
    1. Salvar al más bondadoso
    2. Eliminar al más malvado
    3. Salvar los del rango 10-80
    4. Dejar que el destino decida (random)\n""")
                den = int(input("Ingresa el número de la opción que deseas realizar: "))
                primi.decision(den)
                print("\n⚖️ El juicio ha sido emitido. Fin del Juicio Final.")
                exit()

            elif opc == 6:
                print("Saliendo del modo Datos Primitivos...\n")
                exit()
            else:
                print("Opción no válida, intenta de nuevo.\n")
        except ValueError:
            print("Respuesta no válida, intenta de nuevo.\n")

main()
