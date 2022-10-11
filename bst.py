class BinarySearchTree:
    def __init__(self):
        self._root = self.NullNode()

    def for_each(self, lambda_arg):
        self._root.for_each(lambda_arg)
        # iterate through each element in the tree
        # lambda_arg(tree.val?)

    def insert(self, last_name, first_name, gpa, redID):
        new_node = self.RealNode(last_name, first_name, gpa, redID)
        new_node._left_child = self.NullNode()
        new_node._right_child = self.NullNode()
        self._root = self._root.insert(new_node, self._root)

    class Node:
        def for_each(self):
            pass

        def insert(self, new_node, parent_node):
            pass

        def toString(self):
            pass

    class RealNode(Node):
        def __init__(self, last_name: str, first_name: str, red_id: str, gpa: float):
            self._first_name = first_name
            self._last_name = last_name
            self._red_id = red_id
            self._gpa = gpa
            self._left_child = None
            self._right_child = None

        def toString(self):
            return self._last_name, self._first_name, self._gpa, self._red_id

        def for_each(self, lambda_arg):
            # lambda_arg(current_node)
            print(self._last_name)
            self._left_child.for_each(lambda_arg)
            self._right_child.for_each(lambda_arg)

        def insert(self, new_node, parent_node):
            if new_node._gpa < self._gpa:
                self._left_child = self._left_child.insert(
                    new_node, self._left_child)
            else:
                self._right_child = self._right_child.insert(
                    new_node, self._right_child)
            return parent_node

    class NullNode(Node):

        def for_each(self, lambda_arg):
            return

        def insert(self, new_node, parent_node):
            return new_node

        def toString(self):
            return 'NULL NODE'


tree = BinarySearchTree()
tree.insert('Mikesell', 'Evan', 820215988, 4.0)
tree.insert('A', 'B', 9202, 3.2)
tree.insert('lastname', 'firstname', 9202, 3.4)
print(tree._root.toString())
print(tree._root._left_child.toString())
print(tree._root._left_child._right_child.toString())
print(tree._root._right_child.toString())


tree.for_each(10)
"""
insert
    method in BST
    method in each node class
    checks if greater or less than current node
    if less, recursively call current_node.left.insert(nodeToBeInserted)
    if current_node.left is a nullNode, the insert function sets current_node.left to a nonnull with the gpa, name, redid



strategy:
    declare strategy class
    gpaStrategy, nameStrategy
    pick a strategy (gpa vs name)
    insert method in the node calls strategy.compare(node1,node2), which uses either the gpa comparison between nodes, or the name comparison


visitor: 
    number of null nodes
        use the iterator, each time we visit a null node, count up
    longest path
        ?

"""
