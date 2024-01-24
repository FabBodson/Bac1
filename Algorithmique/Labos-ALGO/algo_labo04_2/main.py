from algo_labo04_2.binary_tree import Node, print_tree


def _main():

    nodes = [89, 120, 52, 31, 11]
    racine = Node(nodes[0])
    racine.root = True
    racine.create_tree(nodes)

    print_tree(racine)

    if racine.has_node(52, racine):
        if racine.suppress_node(52, racine):
            print("Noeud supprimé")

    print_tree(racine)


if __name__ == '__main__':
    _main()
