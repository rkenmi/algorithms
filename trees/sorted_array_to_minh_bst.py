

def sorted_arr_to_minh_bst(A):
    from trees.Tree import BinarySearchTree

    def _make_minh_bst(A, start, end):
        if start > end or start >= len(A):
            return None

        mid = (start + end) // 2
        root = BinarySearchTree(A[mid])
        root.left = _make_minh_bst(A, start, mid-1)
        root.right = _make_minh_bst(A, mid+1, end)

        return root

    return _make_minh_bst(A, 0, len(A))
