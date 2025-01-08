from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = self.isValidBST(root.left)
        right = self.isValidBST(root.right)

        if root.left is None:
            return True if root.right is None else root.val < root.right.val and right
        if root.right is None:
            return root.val > root.left.val and left

        return root.val > root.left.val and root.val < root.right.val and left and right
