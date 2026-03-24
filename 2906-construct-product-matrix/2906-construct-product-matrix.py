class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        result = [[0] * cols for _ in range(rows)]
        MOD = 12345
        suffix_product = 1
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                result[row][col] = suffix_product
                suffix_product = (suffix_product * grid[row][col]) % MOD
        prefix_product = 1
        for row in range(rows):
            for col in range(cols):
                result[row][col] = (result[row][col] * prefix_product) % MOD
                prefix_product = (prefix_product * grid[row][col]) % MOD
        return result