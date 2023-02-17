# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root: return -1
        nodes = []
        min_diff = float('inf')
        q = [root]
        while q:
            cur = q.pop()
            for node in nodes:
                min_diff = min(min_diff, abs(node - cur.val))
            if cur.val not in nodes: nodes.append(cur.val)
            else: return 0
            if cur.left: q.append(cur.left)
            if cur.right: q.append(cur.right)
        return min_diff