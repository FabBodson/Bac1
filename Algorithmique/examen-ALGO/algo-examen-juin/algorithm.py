def node_is_in_tree(root, node_value):
    if node_value < root.value and root.left:
        return node_is_in_tree(root.left, node_value)

    elif node_value > root.value and root.right:
        return node_is_in_tree(root.right, node_value)

    elif node_value == root.value:
        return True

    else:
        return False


def find_smallest_common_ancestor(root, left_child, right_child):
    """
    Recherche dans un arbre binaire 'tree' trié quel est le parent commun le plus proche de deux nœuds et renvoie ce nœud.
    :param root: Node, racine/point de départ dans l'arbre binaire trié dans lequel la recherche sera effectuée.
    :param left_child: Node, premier des deux enfants du nœud recherché.
    :param right_child: Node, deuxième des deux enfants du nœud recherché.
    :return: ancestor, Node, le plus petit ancêtre commun.
    """
    if left_child == right_child:
        return "Children must be different."

    if root.value == left_child or root.value == right_child:
        return "Root cannot be a child."

    if node_is_in_tree(root, left_child) and node_is_in_tree(root, right_child):  # Vérifier que les valeurs demandées sont bien dans l'arbre.
        if left_child < root.value < right_child:
            return root
        else:
            if left_child < root.value and right_child < root.value:
                return find_smallest_common_ancestor(root.left, left_child, right_child)
            else:
                return find_smallest_common_ancestor(root.right, left_child, right_child)

    return "They are not in the tree."
