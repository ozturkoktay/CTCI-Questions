'''
Balanced Binary Tree
Given a binary tree, determine if it is  height-balanced

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true
'''


from typing import Optional


from typing import List, Optional


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0, True  # Base case: height is 0 and it's balanced

        left_height, left_balanced = dfs(node.left)
        right_height, right_balanced = dfs(node.right)

        # Check if current subtree is balanced
        is_balanced = left_balanced and right_balanced and abs(
            left_height - right_height) <= 1

        # Height of the current node
        return max(left_height, right_height) + 1, is_balanced

    _, balanced = dfs(root)
    return balanced


def buildTree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


assert isBalanced(buildTree([3, 9, 20, None, None, 15, 7])) is True
assert isBalanced(buildTree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
assert isBalanced(buildTree([])) is True
