# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []
        def addLeaves(root, leaves):
            if not root:
                return leaves
            if not root.left and not root.right:
                leaves.append(root.val)
            if root.left:
                addLeaves(root.left, leaves)
            if root.right:
                addLeaves(root.right, leaves)
            return leaves
        leaf1 = addLeaves(root1, leaf1)
        leaf2 = addLeaves(root2, leaf2)
        return leaf1 == leaf2
