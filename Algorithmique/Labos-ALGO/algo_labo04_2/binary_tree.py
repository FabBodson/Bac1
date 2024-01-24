def add_children(node):
    child = 0
    if node.right:
        child += 1
    if node.left:
        child += 1
    return child


def successor(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def print_tree(node, file=None, _prefix="", _last=True):
    if node:
        valeur = node.value
    else:
        print("X")
        return
    print(_prefix, "/-" if _last else "|-", valeur, sep="", file=file)
    if _last:
        _prefix += " "
    else:
        _prefix += "| "
    child = [node.right, node.left]
    for test_node in child:
        if test_node:
            _last = add_children(test_node) != 0
            print_tree(test_node, file, _prefix, _last)


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.root = False
        self.left = None
        self.right = None

    def create_tree(self, nodes_to_add):
        for node in range(1, len(nodes_to_add)):
            self.add_node(nodes_to_add[node], self)
        return self

    def add_node(self, new_node_value, current_node):
        if new_node_value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(new_node_value, current_node)
            else:
                self.add_node(new_node_value, current_node.left)
            return self.left
        else:
            if current_node.right is None:
                current_node.right = Node(new_node_value, current_node)
            else:
                self.add_node(new_node_value, current_node.right)
            return self.right

    def has_node(self, node_value, current_node):
        if node_value < current_node.value and current_node.left:
            return self.has_node(node_value, current_node.left)

        elif node_value > current_node.value and current_node.right:
            return self.has_node(node_value, current_node.right)

        elif node_value == current_node.value:
            return current_node

        else:
            return False

    def suppress_node(self, node_to_suppress, root):
        node_to_suppress = self.has_node(node_to_suppress, root)

        if node_to_suppress.left is None and node_to_suppress.right is None:
            if node_to_suppress.parent.value < node_to_suppress.value:
                node_to_suppress.parent.right = None
            else:
                node_to_suppress.parent.left = None
            del node_to_suppress

        elif node_to_suppress.left is not None and node_to_suppress.right is not None:
            successeur = successor(node_to_suppress)
            node_to_suppress.value = successeur.value
            del successeur

        else:
            if node_to_suppress.left is None:
                node_to_suppress.parent.right = None
                del node_to_suppress

            if node_to_suppress.right is None:
                node_to_suppress.parent.left = None
                del node_to_suppress

        return True
