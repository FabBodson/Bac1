class Node:
    def __init__(self, value, parent=None):
        """
        Node content a value, a left node and a right node
        The first node is called root, and its value is set to None
        The parent attribut is usefull to remove a node

        :param value: value to set for a new node
        :param parent: optional parent node
        :return: /
        """
        self.__value = value
        self.__left = None
        self.__right = None
        self.__parent = parent

    def __str__(self):
        return self.__value

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def add_value(self, value):
        """
        adding a node is a recursive object method
        :param value: value to adding to a new node
        :return: None
        """
        if self.__value == value:                           # .4. If value exist, nothing is done
            pass
        elif self.__value > value:
            if self.__left is None:
                self.__left = Node(value, self)
            else:
                self.__left.add_value(value)
        else:
            if self.__right is None:
                self.__right = Node(value, self)
            else:
                self.__right.add_value(value)

    def tree_higher_FULL(self, deph = 0):
        '''
        Question 7 - return multi infos
        OneChild, TwoChild, Sheet, AllNode
        :param deph:
        :return:
        '''
        heigh = 1
        heigher = deph
        OneChild, TwoChild, Sheet = 0, 0, 0
        AllNode = 1
        Ot, Tt, At, St = 0, 0, 0, 0
        O, T, A, S = 0, 0, 0, 0

        if self is None:  # .4. check node is void
            return 0

        if self.__left is not None and self.__right is not None:
            TwoChild = 1
        else:
            if self.__left is not None or self.__right is not None:
                OneChild = 1
            else:
                Sheet = 1
        Ot += OneChild
        Tt += TwoChild
        At += AllNode
        St += Sheet
        if self.__left is not None:
            heigh, O, T, A, S = self.__left.tree_higher_FULL(deph + 1)
            if heigh > heigher:
                heigher = heigh
            Ot += O
            Tt += T
            At += A
            St += S
        if self.__right is not None:
            heigh, O, T, A, S = self.__right.tree_higher_FULL(deph + 1)
            if heigh > heigher:
                heigher = heigh
            Ot += O
            Tt += T
            At += A
            St += S
        return heigher, Ot, Tt, At, St

    def tree_higher(self, deph = 0):
        '''
        Question 6 - return the higher of the tree
        :param deph:
        :return:
        '''
        heigh = 1
        heigher = deph
        if self.__left is not None:
            heigh = self.__left.tree_higher(deph + 1)
            if heigh > heigher:
                heigher = heigh
        if self.__right is not None:
            heigh = self.__right.tree_higher(deph + 1)
            if heigh > heigher:
                heigher = heigh
        return heigher

    def height(self):
        left_height = self.__left.height() if self.__left else 0
        right_height = self.__right.height() if self.__right else 0
        return 1 + max(left_height, right_height)

    def deeper(self, value, deph = 0):
        '''
        Question 5 - return the level of a node
        :param value:
        :param deph:
        :return:
        '''
        deep = -1  # is the value when not found
        if self.__value == value:
            deep = deph
        else:
            if self.__left is not None:
                deep = self.__left.deeper(value, deph+1)
            if deep == -1 and self.__right is not None:
                deep = self.__right.deeper(value, deph+1)
        return deep

    def display_tree(self, deph=0):
        """
        Display the binary tree from the root node
        :return: string
        """
        if self is None:                                                # .4. check node is void
            return 'Node is void'

        CharSpace = 'O.' * deph
        if self.__parent is None:
            parent_value = ''
        else:
            # parent_value = self.__parent.__value
            parent_value = f'Adr.Mem:{id(self.__parent)} - value : {self.__parent.__value} |-| object Adr.Mem:{id(self)} - value:{self.__value}'
        schema = f'{CharSpace} Niv.{deph} : {self.__value} (from {parent_value}) \n'
        if self.__left is not None:
            schema = f'{schema}{CharSpace}\LEFT-{deph:02d}\n '
            schema += self.__left.display_tree(deph+1)
        if self.__right is not None:
            schema = f'{schema}{CharSpace}/RIGHT-{deph:02d}\n '
            schema += self.__right.display_tree(deph+1)
        return schema

    def display_tree_path_patern(self, deph=0, PathPatern=''):
        """
        Display the binary tree from the root node
        :return: string
        """
        schema = f'\ ( L{deph:02d} | {self.__value} ) \n'
        if self.__left is not None:
            NewPathPatern = PathPatern + f'\LFT-{deph:02d}'
            schema += self.__left.display_tree_path_patern(deph+1, NewPathPatern)
        if self.__right is not None:
            NewPathPatern = PathPatern + f'\RGH-{deph:02d}'
            schema += self.__right.display_tree_path_patern(deph+1, NewPathPatern)
        return PathPatern + schema

    def find_node(self, value, depth = 0):
        '''
        Return object node after to found from the param value
        :param value: value of a node to find
        :return: object node or None (if value not found)
        '''
        node_2_find = None
        if self.__value == value:
            node_2_find = self
        else:
            if self.__left is not None:
                node_2_find = self.__left.find_node(value, depth + 1)
            if node_2_find is None and self.__right is not None:
                node_2_find = self.__right.find_node(value, depth + 1)
        return node_2_find

    def grab_node_value_2_list(self, cleanup=False):
        '''
        Grab a tree from a the node object and return it as a collection list
        :return: a collection list of node value(s)
        '''
        list_of_nodes = []
        if self.__left:
            list_of_nodes.extend(self.__left.grab_node_value_2_list())
            if cleanup:
                self.__left = None
        list_of_nodes.append(self.__value)
        if self.__right:
            list_of_nodes.extend(self.__right.grab_node_value_2_list())
            if cleanup:
                self.__right = None
        return list_of_nodes

    def remove_value_CL(self, value):
        node = self.find_node(value)
        if not node:
            return

        parent = node.__parent
        if node is parent.__left:
            parent.__left = None
        else:
            parent.__right = None

        values = []
        if node.__left:
            values.extend(node.__left.grab_node_value_2_list())
        if node.__right:
            values.extend(node.__right.grab_node_value_2_list())

        for value in values:
            parent.add_value(value)

    def remove_value(self, value):
        node_2_find = self.find_node(value)
        if node_2_find is not None:
            if node_2_find.__left is not None:      # Which side to attach at the parent (but left side is preferred) ?
                node_2_attach = node_2_find.__left
                if node_2_find.__right is not None:
                    tree_node_right_side = node_2_find.__right.grab_node_value_2_list()
                else:
                    tree_node_right_side = []
            else:
                if node_2_find.__right is not None:
                    node_2_attach = node_2_find.__right
                else:
                    node_2_attach = None  # not child

            if node_2_find.__parent.__left == node_2_find:          # which side of the parent node ?
                if node_2_attach is not None:
                    node_2_find.__parent.__left = node_2_attach
                    for i in tree_node_right_side:
                        node_2_find.__parent.__left.add_value(i)
                else:                                               # this node is a sheet !
                    del node_2_find.__parent.__left
                    node_2_find.__parent.__left = None
            else:
                if node_2_attach is not None:
                    node_2_find.__parent.__right = node_2_attach
                else:                                               # this node is a sheet !
                    del node_2_find.__parent.__right
                    node_2_find.__parent.__right = None

            # garbage collection clean temporary node object.
