class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1].value


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, t, tree_type):
        if tree_type == "preorder":
            return self.preorder(t.root, "")
        if tree_type == "inorder":
            print(tree_type)
            return self.inorder(t.root, "")
        if tree_type == "postorder":
            print(tree_type)
            return self.postorder(t.root, "")
        if tree_type == "levelorder":
            print(tree_type)
            return self.levelorder(t.root)

    def preorder(self, start, visited):
        """ root -> left -> right """
        if start:
            visited += str(start.value) + "->"
            visited = self.preorder(start.left, visited)
            visited = self.preorder(start.right, visited)
        return visited

    def inorder(self, start, visited):
        """ left -> root -> right """
        print(start.left)
        if start:
            visited = self.inorder(start.left, visited)
            visited += str(start.value) + "->"
            visited = self.inorder(start.right, visited)
        return visited

    def postorder(self, start, visited):
        """ left -> right -> node """
        if start:
            visited = self.postorder(start.left, visited)
            visited = self.postorder(start.right, visited)
            visited += str(start.value) + "->"
        return visited

    def levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        visited = ""
        while len(queue.items) > 0:
            visited += str(queue.peek()) + "->"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return visited


#       100
#     /    \
#    2      3
#   /  \    /\
#  4    5  6  7
#      / \    /\
#     12  77 9   8

tree = BinaryTree(100)
# print(dir(tree.root))
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.right = Node(77)
tree.root.left.right.left = Node(12)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(9)
tree.root.right.right.right = Node(8)

print(tree.print_tree(tree, 'preorder'))
print(tree.print_tree(tree, 'inorder'))
print(tree.print_tree(tree, 'postorder'))
print(tree.print_tree(tree, "levelorder"))
