from algo_labo04.algorithms import has_duplicates
from algo_labo04.binary_tree import Node


def hauteur(node):
    if not node:
        return 0
    left_depth = hauteur(node.left)
    right_depth = hauteur(node.right)
    return 1 + max(left_depth, right_depth)


def add_children(node):
    child = 0
    if node.right:
        child += 1
    if node.left:
        child += 1
    return child


def print_tree(node, file=None, _prefix="", _last=True):
    if node:
        valeur = node.valeur
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


def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def maximum(node):
    if node.right:
        return maximum(node.right)
    else:
        return node.valeur


def minimum(node):
    if node.left:
        return minimum(node.left)
    else:
        return node.valeur


def _main():

    #liste = [89, 120, 52, 31, 11, 92, 77, 71, 145, 46, 83, 9, 14, 65, 75, 79, 85, 76, 69, 78, 80, 86]
    racine = Node(89)
    racine.insert_node(120)
    racine.insert_node(52)
    racine.insert_node(31)
    """
    for element in liste:
        racine.insert_node(element)
"""
    print("Nombre d'enfant(s): ", racine.count_children())

    print_tree(racine)
    print("Nombre de noeuds: ", count_nodes(racine))

    racine = racine.remove_node(31)

    print_tree(racine)
    print("Nombre de noeuds: ", count_nodes(racine))


if __name__ == '__main__':
    _main()
