class BinaryTree:
    def __init__(self, data=0, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def has_value(self, tree):
        if tree is None:
            return False

        return self.data is tree.data

    def print_all(self):
        tree = self
        stack = [tree]
        while len(stack) > 0:  # iterative pre-order traversal
            tree = stack.pop()
            print(tree.data)
            if tree.right:
                stack.append(tree.right)
            if tree.left:
                stack.append(tree.left)


sample = BinaryTree(0)
sample.left = BinaryTree(1)
sample.right = BinaryTree(2)
sample.left.left = BinaryTree(3)
sample.left.right = BinaryTree(4)
# sample.left.left.left = BinaryTree(5)


symmetric_tree = BinaryTree(0)
symmetric_tree.left = BinaryTree(1)
symmetric_tree.left.left = BinaryTree(2)
symmetric_tree.right = BinaryTree(1)
symmetric_tree.right.right = BinaryTree(2)

