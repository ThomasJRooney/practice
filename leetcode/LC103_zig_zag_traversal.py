# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        left = True
        output = []
        q = [root]
        while q:
            out = []
            for i in range(len(q)):
                cur = q.pop(0)
                if left: out.append(cur.val)
                else: out = [cur.val] + out
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            left = not left
            output.append(out)
        return output