class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def create_default_tree():
    """
    This function creates the default tree (see Example 1 or tree-example-1.png).
    :return: Node: the root node of the tree.
    """
    h = Node('H')
    d = h.left = Node('D')
    b = d.left = Node('B')
    a = b.left = Node('A')
    c = b.right = Node('C')
    f = d.right = Node('F')
    e = f.left = Node('E')
    g = f.right = Node('G')
    j = h.right = Node('J')
    i = j.left = Node('I')
    k = j.right = Node('K')
    return h


def display_tree(node, level=0):
    """
    This function displays a tree
    :param node: Node: the node used as tree root for display.
    :param level: int, the level of node in the tree.
    """
    if node is None:
        return

    if level > 0:
        for _ in range(level-1):
            print('|   ', end='')
        print(f'|-- ', end='')
    print(node.value)
    display_tree(node.left, level + 1)
    display_tree(node.right, level + 1)
