class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def translate(index):
            i = index // (len(matrix[0]))
            j = index % len(matrix[0])
            return i,j
        l=0
        r=len(matrix)*len(matrix[0])-1
        while l <= r:
            m = l+(r-l)//2
            i,j = translate(m)
            if matrix[i][j] < target:
                l = m+1
            elif matrix[i][j] > target:
                r = m-1
            else:
                return True
        return False