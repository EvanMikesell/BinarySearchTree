class BinarySearchTree:

    def __init__(self, strategy: 'Strategy'):
        self._strategy = strategy
        self._root = NullNode()

    def for_each(self, lambda_function) -> None:
        self._root.for_each(lambda_function)

    def insert(
            self, first_name: str, last_name: str,
            red_id: int, gpa: float) -> None:
        new_student = Student(first_name, last_name, red_id, gpa)
        self._root = self._root.insert(new_student, self._strategy)

    def accept(self, visitor: 'Visitor') -> None:
        self._root.accept(visitor)

    def search(self, first_name: str, last_name: str,
               red_id: int, gpa: float) -> bool:
        """
        Returns true if a student with the same unique red id is found, 
        false otherwise.
        """
        key_node = Student(first_name, last_name, red_id, gpa)
        return self._root.search(key_node, self._strategy)


class Node:

    def get_left(self):
        pass

    def get_right(self):
        pass

    def for_each(self):
        pass

    def insert(self, new_student: 'Student',
               order_strategy: 'Strategy') -> 'Student':
        pass

    def search(self, key) -> bool:
        pass

    def accept(self, visitor) -> None:
        pass


class Student(Node):
    def __init__(self, first_name: str, last_name: str, red_id: int, gpa: float):
        self._first_name = first_name
        self._last_name = last_name
        self._red_id = red_id
        self._gpa = gpa
        self._left_child = NullNode()
        self._right_child = NullNode()

    def get_left(self) -> 'Student':
        return self._left_child

    def get_right(self) -> 'Student':
        return self._right_child

    def get_red_id(self) -> int:
        return self._red_id

    def get_gpa(self) -> float:
        return self._gpa

    def get_last_name(self) -> str:
        return self._last_name

    def get_first_name(self) -> str:
        return self._first_name

    def for_each(self, lambda_function) -> None:
        # inorder traversal
        self._left_child.for_each(lambda_function)
        lambda_function(self)
        self._right_child.for_each(lambda_function)

    def insert(
            self, new_student: 'Student',
            order_strategy: 'Strategy') -> 'Student':
        # The chosen strategy dicates how the nodes are compared.
        if order_strategy.compare(new_student, self):
            self._right_child = self._right_child.insert(
                new_student, order_strategy)
        else:
            self._left_child = self._left_child.insert(
                new_student, order_strategy)
        return self

    def search(self, key: 'Student', order_strategy: 'Strategy') -> bool:
        if self.get_red_id() == key.get_red_id():
            return True
        elif order_strategy.compare(key, self):
            return self._right_child.search(key, order_strategy)
        else:
            return self._left_child.search(key, order_strategy)

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_student(self)


class NullNode(Node):

    def get_left(self) -> None:
        return

    def get_right(self) -> None:
        return

    def for_each(self, lambda_function) -> None:
        return

    def insert(
            self, new_student: 'Student', order_strategy: 'Strategy') -> 'Student':
        """ 
        When insert is called on a null node, 
        the new node is inserted at that position
        """
        return new_student

    def search(self, key: 'Student', order_strategy: 'Strategy') -> bool:
        # if search finds a null node, the key is not present in the tree
        return False

    def accept(self, visitor: 'Visitor') -> None:
        visitor.visit_null_node(self)


class Strategy:
    def compare(self, new_student: 'Student', current_student: 'Student') -> bool:
        pass


class NameOrder(Strategy):
    def compare(self, new_student: 'Student', current_student: 'Student') -> bool:
        # with strings: a > b means 'does a come after b alphabetically?'
        if new_student.get_last_name() == current_student.get_last_name():
            return new_student.get_first_name() > current_student.get_first_name()
        else:
            return new_student.get_last_name() > current_student.get_last_name()


class GPAOrder(Strategy):
    def compare(self, new_student: 'Student', current_student: 'Student') -> bool:
        new_student_gpa = round(new_student.get_gpa())
        current_student_gpa = round(current_student.get_gpa())
        if new_student_gpa == current_student_gpa:
            return new_student.get_red_id() > current_student.get_red_id()
        else:
            return new_student.get_gpa() > current_student.get_gpa()


class RedIDOrder(Strategy):
    def compare(self, new_student: 'Student', current_student: 'Student') -> bool:
        return new_student.get_red_id() > current_student.get_red_id()


class Visitor:
    """
    Each node will have an accept function which calls it's visit function. 
    """

    def visit_null_node(self, node: 'NullNode') -> None:
        pass

    def visit_student(self, student: 'Student') -> None:
        pass


class NullCountVisitor(Visitor):

    def __init__(self) -> None:
        self._null_count = 0

    def visit_null_node(self, node: 'NullNode') -> None:
        self._null_count += 1

    def visit_student(self, student: 'Student') -> None:
        student.get_left().accept(self)
        student.get_right().accept(self)

    def get_null_count(self) -> int:
        return self._null_count


class PathVisitor(Visitor):

    def __init__(self) -> None:
        self._longest_path = 0
        self._total_path = 0
        self._current_path = -1
        self._student_count = 0

    def visit_null_node(self, node: 'NullNode') -> None:
        return

    def visit_student(self, student: 'Student') -> None:
        """
        Visit method is called on all student objects in the tree.
        Counts the path length from the root student to each student.
        """
        self._current_path += 1
        self._total_path += self._current_path
        self._longest_path = max(self._longest_path, self._current_path)
        self._student_count += 1
        student.get_left().accept(self)
        student.get_right().accept(self)

        # decrementing current path because we are moving back up the tree
        self._current_path -= 1

    def get_average_path(self) -> float:
        return self._total_path / self._student_count

    def get_longest_path(self) -> int:
        return self._longest_path
