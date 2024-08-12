class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        
        # we will be going through the same paths again and again during brute force or recursion.
        # When doing calucalation, as there is duplication paths, we will use DP to cache the sum
        # as upper values will be dependent on lower values sum. So we will start from the end

        # m-2 because, we need to skip last row as it doesnot have any child. If we add m-1, we need to have checks before reading left and right val
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                # There is always left and right child, so not adding any checks to check if it exists.
                left_val  = triangle[i + 1][j]
                right_val = triangle[i + 1][j + 1]

                triangle[i][j] += min(left_val, right_val)

        return triangle[0][0]