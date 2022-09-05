'''
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # bfs
        q, output = [], []
        if root:
            q = [root]
        while len(q) > 0:
            curLevel = []
            for i in range(len(q)):
                cur = q.pop(0)
                curLevel.append(cur.val)
                for child in cur.children:
                    if child != None:
                        q.append(child)
            output.append(curLevel)
        return output
        
