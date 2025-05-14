class NodeAVL:
    def __init__(self, karma, nombre):
        self.karma = karma
        self.nombre = nombre
        self.left = None
        self.right = None
        self.height = 1



class AVLTree:
    def __init__(self):
        self.root = None

    # Insertar
    def insert(self, karma, nombre):
        self.root = self._insert(self.root, karma, nombre)

    def _insert(self, node, karma, nombre):
        if not node:
            return NodeAVL(karma, nombre)
        
        if karma < node.karma:
            node.left = self._insert(node.left, karma, nombre)
        elif karma > node.karma:
            node.right = self._insert(node.right, karma, nombre)
        else:
            return node  # Karma duplicado, no se inserta

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    # Eliminar
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._get_min(node.right)
                node.value = successor.value
                node.right = self._delete(node.right, successor.value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._rebalance(node)

    # Rebalanceo
    def _rebalance(self, node):
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Rotaciones
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Utilidades
    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Print bonito
    def print_pretty(self):
        if self.root is not None:
            lines, *_ = self._build_tree_string(self.root)
            print("\n" + "\n".join(line.rstrip() for line in lines))
        else:
            print("\nEmpty tree...")

    def _build_tree_string(self, node):
        if node.right is None and node.left is None:
            line = str(node.value)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if node.right is None:
            lines, n, p, x = self._build_tree_string(node.left)
            s = str(node.value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if node.left is None:
            lines, n, p, x = self._build_tree_string(node.right)
            s = str(node.value)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._build_tree_string(node.left)
        right, m, q, y = self._build_tree_string(node.right)
        s = str(node.value)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [' ' * n] * (q - p)
        elif q < p:
            right += [' ' * m] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def _collect_nodes(self, node, lista):
        if node:
            self._collect_nodes(node.left, lista)
            lista.append(node)
            self._collect_nodes(node.right, lista)

    def get_all_nodes(self):
        nodos = []
        self._collect_nodes(self.root, nodos)
        return nodos