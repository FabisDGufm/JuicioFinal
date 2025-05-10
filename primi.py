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
    karma_max = 0
    if (val_kids >= karma_max):
        nom_max = kids
        karma_max = val_kids
    elif(val_ancianos >= karma_max):
        nom_max = ancianos
        karma_max = val_ancianos
    elif(val_politicos >= karma_max):
        nom_max = politicos
        karma_max = val_politicos    
    elif(val_cientificos >= karma_max):
        nom_max = cientificos
        karma_max = val_cientificos
    elif(val_ladrones >= karma_max):
        nom_max = ladrones
        karma_max = val_ladrones
    elif(val_artistas >= karma_max):
        nom_max = artistas
        karma_max = val_artistas
    return(nom_max, karma_max)


def buscar_min():
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
    primero = ""
    segundo = ""
    tercero = ""
    cuarto = ""
    quinto = ""
    sexto = ""
    
    print()
    
def decision():
    print()