import unittest
import bst


class TestBST(unittest.TestCase):
    def setUp(self):
        self.name_tree = self.fill_tree(bst.BinarySearchTree(bst.NameOrder()))

    def get_all_names(self, tree: 'bst.BinarySearchTree') -> list:
        # visits each node with an inorder traversal and returns a list of names.
        inorder_names = []
        def create_name_list(student): return inorder_names.append(
            student.get_first_name() + " " + student.get_last_name())
        tree.for_each(create_name_list)
        return inorder_names

    def fill_tree(self, tree: 'bst.BinarySearchTree') -> 'bst.BinarySearchTree':
        tree.insert('Evan', 'Mikesell', 820215988, 2)
        tree.insert('John', 'Mikesell', 920215988, 3.5)
        tree.insert('First', 'Last', 310613686, 1)
        tree.insert('Anika', 'Samuel', 731389042, 0.1)
        tree.insert('Jo', 'Castro', 111389042, 3.5)
        tree.insert('Kalum', 'Rowland', 931389042, -1)
        tree.insert('John', 'Z', 230459192, 4)
        return tree

    def test_search(self):
        self.assertTrue(self.name_tree.search(
            'Evan', 'Mikesell', 820215988, 2))

    def test_search_fail(self):
        self.assertFalse(self.name_tree.search(
            'Evan', 'Mikesell', 520215988, 2))

    def test_for_each(self):
        basic_tree = bst.BinarySearchTree(bst.NameOrder())
        basic_tree.insert('A', 'B', 820215988, 2)
        basic_tree.insert('C', 'D', 920215988, 3.5)
        basic_tree.insert('E', 'F', 310613686, 1)
        correct_names = ['A B', 'C D', 'E F']
        inorder_names = self.get_all_names(basic_tree)
        self.assertEqual(correct_names, inorder_names)

    def test_red_id_strategy(self):
        red_id_tree = self.fill_tree(
            bst.BinarySearchTree(bst.RedIDOrder()))
        correct_name_order = ['Jo Castro', 'John Z', 'First Last',
                              'Anika Samuel', 'Evan Mikesell',
                              'John Mikesell', 'Kalum Rowland']
        inorder_names = self.get_all_names(red_id_tree)
        self.assertEqual(inorder_names, correct_name_order)

    def test_gpa_strategy(self):
        gpa_tree = self.fill_tree(bst.BinarySearchTree(bst.GPAOrder()))
        correct_name_order = ['Kalum Rowland', 'Anika Samuel', 'First Last',
                              'Evan Mikesell', 'Jo Castro',
                              'John Z', 'John Mikesell']
        inorder_names = self.get_all_names(gpa_tree)
        self.assertEqual(inorder_names, correct_name_order)

    def test_name_strategy(self):
        correct_name_order = ['Jo Castro', 'First Last', 'Evan Mikesell',
                              'John Mikesell', 'Kalum Rowland',
                              'Anika Samuel', 'John Z']
        inorder_names = self.get_all_names(self.name_tree)
        self.assertEqual(inorder_names, correct_name_order)

    def test_path_length_visitor(self):
        correct_average_path = 1.714285714
        path_visitor = bst.PathVisitor()
        self.name_tree.accept(path_visitor)
        self.assertAlmostEqual(
            path_visitor.get_average_path(), correct_average_path)

    def test_longest_path(self):
        correct_longest_path = 3
        path_visitor = bst.PathVisitor()
        self.name_tree.accept(path_visitor)
        self.assertEqual(path_visitor.get_longest_path(), correct_longest_path)

    def test_null_count_visitor(self):
        correct_null_count = 8
        null_count_visitor = bst.NullCountVisitor()
        self.name_tree.accept(null_count_visitor)
        self.assertEqual(null_count_visitor.get_null_count(),
                         correct_null_count)


if __name__ == '__main__':
    unittest.main()
