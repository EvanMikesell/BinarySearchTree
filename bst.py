from xmlrpc.client import Boolean


class BinarySearchTree:
    # strategy = GPAOrder() TO do now : figure out how to do the strategy method
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

        def get_gpa(self):
            return self._gpa

        def get_last_name(self):
            return self._last_name

        def get_first_name(self):
            return self._first_name

        def for_each(self, lambda_arg):
            lambda_arg(self)
            self._left_child.for_each(lambda_arg)
            self._right_child.for_each(lambda_arg)

        def insert(self, new_node, parent_node):

            # replace this comparison with strategy comparison method
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


class Strategy:
    def greater_than(node1, node2):
        pass


class GPAOrder(Strategy):
    def greater_than(self, node1, node2) -> bool:
        if node1.get_gpa() > node2.get_gpa():
            return True
        else:
            return False


class NameOrder(Strategy):
    def greater_than(self, node1, node2) -> bool:
        # x<y means "does x come before y alphabetically?"
        if node1.get_last_name() == node2.get_last_name():
            if node1.get_first_name() < node1.get_first_name():
                return True
            else:
                return False

        elif node1._last_name < node2._last_name:
            return True
        else:
            return False


tree = BinarySearchTree()
tree.insert('Mikesell', 'Evan', 820215988, 4.0)
tree.insert('Mikesell', 'B', 9202, 3.2)
tree.insert('lastname', 'firstname', 9202, 3.4)


def x(a): return print(a._last_name)
# tree.for_each(x)


name_strategy = NameOrder()
gpa_strategy = GPAOrder()
print("two nodes:")
print(tree._root.toString())
print(tree._root._left_child.toString())
print(name_strategy.greater_than(tree._root, tree._root._left_child))  # false
print(gpa_strategy.greater_than(tree._root, tree._root._left_child))  # true


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
