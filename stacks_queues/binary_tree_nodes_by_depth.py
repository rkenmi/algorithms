

def binary_tree_nodes_by_depth(root):
    from copy import copy

    sub_q = [root]
    q = [sub_q]
    nodes_by_depth = [[root]]

    while q:
        sub_q = q.pop(0)

        new_nodes = []
        while sub_q:
            node = sub_q.pop(0)
            if node.left:
                new_nodes.append(node.left)

            if node.right:
                new_nodes.append(node.right)

        if new_nodes:
            q.append(new_nodes)
            nodes_by_depth.append(copy(new_nodes))

    return nodes_by_depth

def binary_tree_nodes_by_depth_imp(root):
    from copy import copy

    sub_q = [root]
    q = [sub_q]
    nodes_by_depth = [[root]]

    while q:
        sub_q = q.pop(0)

        new_nodes = []
        while sub_q:
            node = sub_q.pop(0)
            if node.left:
                new_nodes.append(node.left)

            if node.right:
                new_nodes.append(node.right)

        if new_nodes:
            q.append(new_nodes)
            nodes_by_depth.append(copy(new_nodes))

    return nodes_by_depth


