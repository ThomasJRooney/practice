class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Initialize the matrix with -1
        mat = [[-1 for _ in range(n)] for _ in range(m)]        
        
        # Define the boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        cur = head
        while cur and top <= bottom and left <= right:
            # Traverse right
            for j in range(left, right + 1):
                if cur:
                    mat[top][j] = cur.val
                    cur = cur.next
                else:
                    return mat
            top += 1
            
            # Traverse down
            for i in range(top, bottom + 1):
                if cur:
                    mat[i][right] = cur.val
                    cur = cur.next
                else:
                    return mat
            right -= 1
            
            if top <= bottom:
                # Traverse left
                for j in range(right, left - 1, -1):
                    if cur:
                        mat[bottom][j] = cur.val
                        cur = cur.next
                    else:
                        return mat
                bottom -= 1
            
            if left <= right:
                # Traverse up
                for i in range(bottom, top - 1, -1):
                    if cur:
                        mat[i][left] = cur.val
                        cur = cur.next
                    else:
                        return mat
                left += 1
        
        return mat
