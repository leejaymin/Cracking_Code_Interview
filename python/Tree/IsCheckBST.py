def checkBST(root):
    # traversal by inOrder
    resList = []
    resList = inOrder(root, resList)
    sortedList = sorted(resList)

    if len(set(resList)) != len(resList):
        return False

    if len([i for i, j in zip(resList, sortedList) if i == j]) == len(resList):
        return True
    else:
        return False

def inOrder(node, resList):
    if node.left is not None:
        resList = inOrder(node.left, resList)
    resList.append(node.data)
    if node.right is not None:
        resList = inOrder(node.right, resList)
    return resList