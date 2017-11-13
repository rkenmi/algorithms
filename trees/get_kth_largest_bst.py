def kth_largest_reverse_inorder(root, k):
    """
        Basically the inverse of kth_smallest_inorder.
        Since we are BACKTRACKING the inorder traversal (after going to the rightmost/largest node),
        this is RNL instead of LNR.
    :param root:
    :param k:
    :return:
    """
    def _rnl_k(root, k):
        if root and k > 0:
            node, k = _rnl_k(root.right, k)  # <-- R
            if node:
                return node, k

            k -= 1  # <-- N
            if k == 0:
                return root, k

            if root.left and k > 0:
                node, k = _rnl_k(root.left, k)  # <-- L
                if node:
                    return node, k

        return None, k

    return _rnl_k(root, k)[0] if k > 0 else root
