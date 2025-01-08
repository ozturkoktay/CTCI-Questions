'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
'''


from typing import Optional


from typing import List, Optional


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def successor(lst: list, p: int):
    pass


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


assert successor(buildTree([3, 9, 20, None, None, 15, 7])) is True
assert successor(buildTree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
assert successor(buildTree([])) is True
