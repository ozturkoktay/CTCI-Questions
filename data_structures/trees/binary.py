class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#     1
#    / \
#   2   3
#  / \
# 4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

"""

1. Inorder Traversal (Left, Root, Right):
    Example: 4, 2, 5, 1, 3

2. Preorder Traversal (Root, Left, Right):
    Example: 1, 2, 4, 5, 3
    
3. Postorder Traversal (Left, Right, Root):
    Example: 4, 5, 2, 3, 1

"""

result = []


def inorder(root):
    if not root:
        return []

    inorder(root.left)
    result.append(root.val)
    inorder(root.right)
    return result


def preorder(root):
    if not root:
        return []

    result.append(root.val)
    preorder(root.left)
    preorder(root.right)
    return result


def postorder(root):
    if not root:
        return []

    postorder(root.left)
    postorder(root.right)
    result.append(root.val)
    return result
