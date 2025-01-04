class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def kthSmall(root, k):

    if k == root.val:
        return k
    else:
        kthSmall(root, k)


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

print(kthSmall(root, 3))
