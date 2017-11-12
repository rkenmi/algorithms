def kth_smallest_aug(root, k):
    """
        This solution assumes that the BST is augmented with a num_nodes property/attribute,
        where each node tracks the number of children it has.
    :param root:
    :param k:
    :return:
    """
    if not root:
        return

    leftnum = 0
    if root.left:
        leftnum = root.left.count

    if leftnum + 1 == k:
        return root

    if leftnum < k:
        return kth_smallest_aug(root.right, k-1-leftnum)
    else:
        return kth_smallest_aug(root.left, k)

def kth_smallest_inorder(root, k):
    """
        In-order (LNR) traversal gives us sorted elements.
        We can make use of this to get the kth smallest element.
        Notice that we do the k-1 operation in the middle, where we choose to *process* the node (middle of LNR)

        This is a good algorithm and doesn't need BST augmentation.
        With that said however, the worst case time complexity O(n) and space complexity O(n) is easier to hit
        especially if k is a number that is close to the max. number of nodes in tree.

        The BST augmentation algorithm will perform better on average.
    :param root:
    :param k:
    :return:
    """
    def _lnr_k(root, k):
        if root and k > 0:
            node, k = _lnr_k(root.left, k)  # <-- L
            if node:
                return node, k

            k -= 1  # <-- N
            if k == 0:
                return root, k

            if root.right and k > 0:
                node, k = _lnr_k(root.right, k)  # <-- R
                if node:
                    return node, k

        return None, k

    return _lnr_k(root, k)[0]

