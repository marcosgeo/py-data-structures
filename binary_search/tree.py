
class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, key, name):
        new_node = Node(key, name)
        if self.root is None:
            self.root = new_node
            return True
        else:
            focus_node = self.root
            while True:
                parent = focus_node
                if key < focus_node.key:
                    focus_node = focus_node.left_child
                    if focus_node is None:
                        parent.left_child = new_node
                        return True
                else:
                    focus_node = focus_node.right_child
                    if focus_node is None:
                        parent.right_child = new_node
                        return True

    def in_order_traverse(self, focus_node):
        if focus_node is not None:
            self.in_order_traverse(focus_node.left_child)
            print(focus_node)
            self.in_order_traverse(focus_node.right_child)

    def preorder_traverse(self, focus_node):
        if focus_node is not None:
            print(focus_node)
            self.preorder_traverse(focus_node.left_child)
            self.preorder_traverse(focus_node.right_child)

    def postorder_traverse(self, focus_node):
        if focus_node is not None:
            self.postorder_traverse(focus_node.left_child)
            self.postorder_traverse(focus_node.right_child)
            print(focus_node)

    def find(self, key):
        focus_node = self.root
        while focus_node.key != key:
            if key < focus_node.key:
                focus_node = focus_node.left_child
            else:
                focus_node = focus_node.right_child
            if focus_node is None:
                return None
        return focus_node

class Node:
    def __init__(self, key=0, name=""):
        self.key = key
        self.name = name
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.name} has the key {self.key}"


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_node(50, "Boss")
    tree.add_node(25, "Vice President")
    tree.add_node(15, "Office Manager")
    tree.add_node(30, "Secretary")
    tree.add_node(75, "Sales Manager")
    tree.add_node(85, "Salesperson")

    tree.in_order_traverse(tree.root)
    print()
    tree.preorder_traverse(tree.root)
    print()
    tree.postorder_traverse(tree.root)
    print()
    print(tree.find(85))
    print(tree.find(9))
    print()
