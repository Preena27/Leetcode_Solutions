class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Calculate the total sum of all elements in the grid
        total_sum = sum(sum(row) for row in grid)
      
        # If total sum is odd, we cannot partition into two equal halves
        if total_sum % 2:
            return False
      
        # Target sum for each partition (half of total)
        target_sum = total_sum // 2
      
        # Check if we can partition by cutting between rows
        prefix_sum = 0
        for i, row in enumerate(grid):
            prefix_sum += sum(row)
            # If prefix sum equals target and we're not at the last row
            # we found a valid horizontal partition
            if prefix_sum == target_sum and i != len(grid) - 1:
                return True
      
        # Check if we can partition by cutting between columns
        prefix_sum = 0
        # Transpose the grid to iterate through columns
        for j, column in enumerate(zip(*grid)):
            prefix_sum += sum(column)
            # If prefix sum equals target and we're not at the last column
            # we found a valid vertical partition
            if prefix_sum == target_sum and j != len(grid[0]) - 1:
                return True
      
        # No valid partition found
        return False 