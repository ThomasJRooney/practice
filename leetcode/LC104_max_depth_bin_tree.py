# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if not root: return ret
        q = [root]
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            ret += 1
        return ret
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret = 0
        if not root: return ret
        q = [root]
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            ret += 1
        return ret