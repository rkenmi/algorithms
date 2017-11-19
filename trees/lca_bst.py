def lca_bst(root, A, B):
    if not root:
        return None

    if root.data < min(A.data, B.data):
        return lca_bst(root.right, A, B)

    if root.data > max(A.data, B.data):
        return lca_bst(root.left, A, B)

    return root
