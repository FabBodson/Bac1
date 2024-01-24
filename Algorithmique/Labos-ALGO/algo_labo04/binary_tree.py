class Node:
    def __init__(self, valeur, parent=None):
        self.valeur = valeur
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.valeur)

    def count_children(self):
        return bool(self.right) + bool(self.left)

    def insert_node(self, new_node):
        if new_node < self.valeur:
            if self.left is None:
                self.left = Node(new_node, self)
            else:
                self.left.insert_node(new_node)
        elif new_node > self.valeur:
            if self.right is None:
                self.right = Node(new_node, self)
            else:
                self.right.insert_node(new_node)

    def remove_node(self, node_to_suppress):
        if node_to_suppress < self.valeur:
            self.left.remove_node(node_to_suppress)

        elif node_to_suppress > self.valeur:
            self.right.remove_node(node_to_suppress)

        else:
            if self == self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None
                
            del self.valeur
            print("supprimé")
