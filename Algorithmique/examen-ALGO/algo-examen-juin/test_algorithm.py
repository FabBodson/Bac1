import unittest

from algorithm import find_smallest_common_ancestor
from custom_tree import create_default_tree, Node


class FindSmallerCommonAncestorTest(unittest.TestCase):
    tree = create_default_tree()

    def test_finds_ancestor(self):
        ancestor_b = find_smallest_common_ancestor(self.tree, 'A', 'C')
        ancestor_d = find_smallest_common_ancestor(self.tree, 'C', 'F')
        ancestor_h = find_smallest_common_ancestor(self.tree, 'E', 'K')

        node_b = Node('B')
        node_d = Node('D')
        node_h = Node('H')

        self.assertEqual(node_b.value, ancestor_b.value)
        self.assertEqual(node_d.value, ancestor_d.value)
        self.assertEqual(node_h.value, ancestor_h.value)

    def test_is_not_a_child(self):
        ancestor_1 = find_smallest_common_ancestor(self.tree, 'W', 'Z')
        ancestor_2 = find_smallest_common_ancestor(self.tree, 'A', 'Z')

        self.assertEqual("They are not in the tree.", ancestor_1)
        self.assertEqual("They are not in the tree.", ancestor_2)

    def test_root_value_is_different_of_children(self):
        ancestor_1 = find_smallest_common_ancestor(self.tree, 'J', 'I')
        ancestor_2 = find_smallest_common_ancestor(self.tree, 'B', 'D')

        self.assertEqual("Root cannot be a child.", ancestor_1)
        self.assertEqual("Root cannot be a child.", ancestor_2)

    def test_same_children(self):
        ancestor_1 = find_smallest_common_ancestor(self.tree, 'J', 'J')
        ancestor_2 = find_smallest_common_ancestor(self.tree, 'H', 'H')

        self.assertEqual("Children must be different.", ancestor_1)
        self.assertEqual("Children must be different.", ancestor_2)
