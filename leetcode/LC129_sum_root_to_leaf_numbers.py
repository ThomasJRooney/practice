# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def get_paths(paths, num_str, node):
            if node: num_str += str(node.val)
            if not node.left and not node.right: paths.append(int(num_str))
            if node.left: get_paths(paths, num_str, node.left)
            if node.right: get_paths(paths, num_str, node.right)
            return paths
        return(sum(get_paths([], "", root)))
        #return(sum(get_paths([], "", root)))