class BinaryTree:
    def __init__(self, data=0, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __eq__(self, tree):
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


class BinarySearchTree(BinaryTree):

    def add(self, node):
        parent = None
        root = self
        while root:
            parent = root
            if node.data < root.data:
                root = root.left
            elif node.data >= root.data:
                root = root.right

        if node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

    def get(self, key):
        # key is just node.data in this case
        root = self
        while root:
            if key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
            else:  # root.data = key
                return root


    def remove(self, key):
        # key is just node.data in this case
        parent = None
        root = self
        while root:
            if key < root.data:
                parent = root
                root = root.left
            elif key > root.data:
                parent = root
                root = root.right
            else:  # root.data = key. found the node.
                """
                if this node has no children: set the parent's pointer to this node to be null
                if this node only has right children: we'll need to add it to parent.right
                if this node only has left children: we'll need to add it to parent.right
                if this node has both left and right children: find the first node in the 
                    left subtree (call it 1N) and pick the farthest right node in 1N's right subtree 
                    (i.e. the largest node in left subtree) to be parent.right, then attach the deleted node's right
                    children to that parent.right's right subtree and attach 1N's left subtree to parent.right's
                    left subtree.
                """
                if root.left is None and root.right is None:
                    if root.data < parent.data:
                        parent.left = None
                    else:
                        parent.right = None
                    return root

                if root.left is None and root.right is not None or \
                    root.right is None and root.left is not None:
                    parent.right = root.left or root.right

                # Root has both left and right children
                temp = left_node = root.left

                # Go all the way right until you hit the parent of the farthest right node
                while temp and temp.right and temp.right.right:
                    temp = temp.right

                replacement = temp.right if temp.right else temp  # if no right children, then current node is largest

                temp.right = None  # cut the pointer
                replacement.left = left_node
                replacement.right = root.right  # deleted node's right subtree
                parent.right = replacement

                return root











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

