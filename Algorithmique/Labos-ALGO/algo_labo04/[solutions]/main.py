from algorithms import has_duplicates_1, has_duplicates_2, has_duplicates_3
from binary_tree import Node

def main():

#    title_1 = "Bonjour, recherche un doublon dans une liste."
#    asking = "Entrer une liste de valeurs séparées un espace : "
#    reply = "Votre liste contient-elle une doublon ? "
#    print(title_1)
#    list_check = input(asking).split()
#    print("01." + reply, has_duplicates_1(list_check))
#    print("02." + reply, has_duplicates_2(list_check))
#    print("03." + reply, has_duplicates_3(list_check))

    title_1 = "Les arbres binaires"
    my_node = None
    for i in range(1,int(input("combien de noeud voulez-vous ajouter ? "))+1):
        new_value = int(input(f'Entrer une valeur pour votre noeud [{i}] : '))
        if i == 1:
            my_node = Node(new_value)
        else:
            my_node.add_value(new_value)

    print("Test unitaire - tableau de 1 - 20,18,17,19,25,15")
    TestTab1 = [20, 18, 17, 19, 25, 15]
    for i in range(len(TestTab1)):
        print(f'add : {TestTab1[i]}')
        if i == 0:
            my_node = Node(int(TestTab1[i]))
        else:
            my_node.add_value(int(TestTab1[i]))

    print(my_node.display_tree())
    print("-#" * 10 + "\n")
    print(my_node.display_tree_path_patern())

    for i in range(0,3):
        a = int(input(f"5. Profondeur d'un noeud - cas {i} - entrez un noeud : "))
        print(my_node.deeper(a))
    heigh = my_node.tree_higher()
    print(f"6. La hauteur de l'arbre : {heigh}")

    print("Suppression d'un noeud")
    DELETE = int(input("entrer la valeur du noeud à supprimer :"))
    print(my_node.remove_value(DELETE))

    print ("#-" * 5 + "Nouvelles valeurs de l'arbre" + "-#"*5)
    print(my_node.display_tree())
    print("-#" * 10 + "\n")
    print(my_node.display_tree_path_patern())


    print("Test unitaire - tableau II  - 20,15,25,19,17,11,14,7,22,50")
    del my_node
    TestTab1 = [20, 15, 25, 19, 17, 11, 14, 7, 22, 50]
    for i in range(len(TestTab1)):
        print(f'add : {TestTab1[i]}')
        if i == 0:
            my_node = Node(TestTab1[i])
        else:
            my_node.add_value(TestTab1[i])

    print(my_node.display_tree())
    print("-#" * 10 + "\n")
    print(my_node.display_tree_path_patern())


    for i in range(0, 3):
        a = int(input(f"5. Profondeur d'un noeud - cas {i} - entrez un noeud : "))
        print(my_node.deeper(a))
    heigh = my_node.tree_higher()
    print(f"6. La hauteur de l'arbre : {heigh}")

    print("Suppression d'un noeud")
    DELETE = int(input("entrer la valeur du noeud à supprimer :"))
    print(my_node.remove_value_CL(DELETE))

    print("#-" * 5 + "Nouvelles valeurs de l'arbre" + "-#" * 5)
    print(my_node.display_tree())
    print("-#" * 10 + "\n")
    print(my_node.display_tree_path_patern())

    for i in range(0, 3):
        a = int(input(f"5. Profondeur d'un noeud - cas {i} - entrez un noeud : "))
        print(my_node.deeper(a))
    heigh = my_node.tree_higher()
    print(f"6. La hauteur de l'arbre : {heigh}")

    print(f' 7. statistique ')
    a,b,c,d,e = my_node.tree_higher_FULL()
    print("Tous les noeuds : {} \n Tous les noeuds avec 2 fils : {} \n Tous les noeuds avec 1 fils : {} \n Toutes les feuilles : {} ".format(d,c,b,e))


if __name__ == '__main__':
    main()



