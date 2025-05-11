import random
from tree import NodeAVL, AVLTree
tree = AVLTree()

def insert():
    grupos = ["Kids", "Ancianos", "Politicos", "Cientificos", "Ladrones", "Artistas"]
    
    for nombre in grupos:
        karma = random.randint(-100, 100)  # ahora el karma va de -100 a 100
        tree.insert(karma, nombre)
        print(f"{nombre} fue asignado con karma {karma}")


def buscar_max():
    if not tree.root:
        return None
    
    current_node = tree.root
    
    while current_node.right:
        current_node = current_node.right
    
    return(current_node.nombre, current_node.karma)

def buscar_min():
    if not tree.root:
        return None
    
    current_node = tree.root
    
    while current_node.left:
        current_node = current_node.left
    return(current_node.nombre, current_node.karma)

def buscar_rango():
    inf = 10
    sup = 80
    print(f"Grupos con karma entre {inf} y {sup}:")
    encontrados = []
    _buscar_rango(tree.root, inf, sup, encontrados)

    if not encontrados:
        print("No existe grupo que esté dentro de ese intervalo de karma.\n")

def _buscar_rango(node, inf, sup, encontrados):
    if not node:
        return

    if inf < node.karma:
        _buscar_rango(node.left, inf, sup, encontrados)

    if inf <= node.karma <= sup:
        print(f"{node.nombre} (karma: {node.karma})")
        encontrados.append(node)

    if node.karma < sup:
        _buscar_rango(node.right, inf, sup, encontrados)




def inorder():
    print("Recorrido in-order del árbol (de mayor a menor):")
    _inorder(tree.root)
    

def _inorder(node):
    if node:
        _inorder(node.right)
        print(f"Grupo: {node.nombre} | Karma: {node.karma}")
        _inorder(node.left)
   

def decision(den):
    if (den == 1):
        print()

def aleatorio():
    print()