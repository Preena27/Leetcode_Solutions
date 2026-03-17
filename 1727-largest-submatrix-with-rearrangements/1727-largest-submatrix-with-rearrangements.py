class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [[0] * n for _ in range(m)]
        for j in range(n):
            heights[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1
                else:
                    heights[i][j] = 0
        max_area = 0
        for row in heights:
            row.sort(reverse=True)
            for k, h in enumerate(row):
                max_area = max(max_area, h * (k + 1))
        return max_area

        