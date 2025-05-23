import random

kids = "Niños"
ancianos = "Ancianos"
politicos = "Políticos"
cientificos = "Científicos"
ladrones = "Ladrones"
artistas = "Artistas"

val_kids = val_ancianos = val_politicos = val_cientificos = val_ladrones = val_artistas = 0

def insert():
    global val_kids, val_ancianos, val_politicos, val_cientificos, val_ladrones, val_artistas

    val_kids = random.randint(-100, 100)
    val_ancianos = random.randint(-100, 100)
    val_politicos = random.randint(-100, 100)
    val_cientificos = random.randint(-100, 100)
    val_ladrones = random.randint(-100, 100)
    val_artistas = random.randint(-100, 100)

    print(f"{kids} - Karma: {val_kids}")
    print(f"{ancianos} - Karma: {val_ancianos}")
    print(f"{politicos} - Karma: {val_politicos}")
    print(f"{cientificos} - Karma: {val_cientificos}")
    print(f"{ladrones} - Karma: {val_ladrones}")
    print(f"{artistas} - Karma: {val_artistas}")
    print()

def buscar_max():
    global kids, val_kids, ancianos, val_ancianos, politicos, val_politicos, cientificos, val_cientificos, ladrones, val_ladrones, artistas, val_artistas
    nom_max = ""
    karma_max = -101
    if (val_kids >= karma_max):
        nom_max = kids
        karma_max = val_kids
    if(val_ancianos >= karma_max):
        nom_max = ancianos
        karma_max = val_ancianos
    if(val_politicos >= karma_max):
        nom_max = politicos
        karma_max = val_politicos    
    if(val_cientificos >= karma_max):
        nom_max = cientificos
        karma_max = val_cientificos
    if(val_ladrones >= karma_max):
        nom_max = ladrones
        karma_max = val_ladrones
    if(val_artistas >= karma_max):
        nom_max = artistas
        karma_max = val_artistas
    return(nom_max, karma_max)


def buscar_min():

    global kids, val_kids, ancianos, val_ancianos, politicos, val_politicos, cientificos, val_cientificos, ladrones, val_ladrones, artistas, val_artistas
    nom_min = ""
    karma_min = 101  # Valor más alto posible
    if (val_kids <= karma_min):
        nom_min = kids
        karma_min = val_kids
    if (val_ancianos <= karma_min):
        nom_min = ancianos
        karma_min = val_ancianos
    if (val_politicos <= karma_min):
        nom_min = politicos
        karma_min = val_politicos
    if (val_cientificos <= karma_min):
        nom_min = cientificos
        karma_min = val_cientificos
    if (val_ladrones <= karma_min):
        nom_min = ladrones
        karma_min = val_ladrones
    if (val_artistas <= karma_min):
        nom_min = artistas
        karma_min = val_artistas
    return (nom_min, karma_min)

    print()

def buscar_rango():
    min = 10
    max = 80
    encontrado = 0
    if (min <= val_kids <= max):
        print(f"{kids} - Karma: {val_kids}")
        encontrado = 1
    if(min <= val_ancianos <= max):
        print(f"{ancianos} - Karma: {val_ancianos}")
        encontrado = 1
    if(min <= val_politicos <= max):
        print(f"{politicos} - Karma: {val_politicos}")  
        encontrado = 1
    if(min <= val_cientificos <= max):
        print(f"{cientificos} - Karma: {val_cientificos}")
        encontrado = 1
    if(min <= val_ladrones <= max):
        print(f"{ladrones} - Karma: {val_ladrones}")
        encontrado = 1
    if(min <= val_artistas <= max):
        print(f"{artistas} - Karma: {val_artistas}")
        encontrado = 1
    if encontrado == 0:
        print("No existe grupo que esté dentro de ese intervalo de karma")
    print()

def inorder():
    global kids, val_kids, ancianos, val_ancianos, politicos, val_politicos, cientificos, val_cientificos, ladrones, val_ladrones, artistas, val_artistas

    g1, v1 = kids, val_kids
    g2, v2 = ancianos, val_ancianos
    g3, v3 = politicos,val_politicos
    g4, v4 = cientificos, val_cientificos
    g5, v5 = ladrones, val_ladrones
    g6, v6 = artistas, val_artistas

    print("Recorrido in-order (de mayor a menor):")

    for i in range(6):
        karma_max = -101
        gM = ""
        if (v1 >= karma_max):
            gM = g1
            karma_max = v1
        if(v2 >= karma_max):
            gM = g2
            karma_max = v2
        if(v3 >= karma_max):
            gM = g3
            karma_max = v3    
        if(v4 >= karma_max):
            gM = g4
            karma_max = v4
        if(v5 >= karma_max):
            gM = g5
            karma_max = v5
        if(v6 >= karma_max):
            gM = g6
            karma_max = v6

        print(f"Grupo: {gM} | Karma: {karma_max}")

        if (gM == g1):
            v1 = -1000
        elif (gM == g2):
            v2 = -1000
        elif (gM == g3):
            v3 = -1000
        elif (gM == g4):
            v4 = -1000
        elif (gM == g5):
            v5 = -1000
        elif (gM == g6):
            v6 = -1000    
    print()
    
def aleatorio():
    
    opcion = random.randint(1, 6)

    if opcion == 1:
        elegido = kids
    elif opcion == 2:
        elegido = ancianos
    elif opcion == 3:
        elegido = politicos
    elif opcion == 4:
        elegido = cientificos
    elif opcion == 5:
        elegido = ladrones
    elif opcion == 6:
        elegido = artistas

    print(f"El grupo salvado es '{elegido}'\n")
    
    
def decision(den):
    if den == 1:
        nombre, karma = buscar_max()
        print(f"🟢 Has decidido salvar al grupo más bondadoso: {nombre} con karma {karma}")
    elif den == 2:
        nombre, karma = buscar_min()
        print(f"🔴 Has decidido eliminar al grupo más malvado: {nombre} con karma {karma}")
    elif den == 3:
        print("🟡 Has decidido salvar los grupos con karma entre 10 y 80:")
        buscar_rango()
    elif den == 4:
        print("⚖️ Has decidido dejar que el destino decida:")
        aleatorio()
    