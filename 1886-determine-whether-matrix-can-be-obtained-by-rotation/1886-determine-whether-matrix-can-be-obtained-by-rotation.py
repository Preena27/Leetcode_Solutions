class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:      
        def rotate_90_clockwise(matrix: List[List[int]]) -> None:
            n = len(matrix)
          
            # Process the matrix layer by layer from outside to inside
            for layer in range(n // 2):
                # Define the boundaries of the current layer
                first = layer
                last = n - 1 - layer
              
                # Rotate elements in the current layer
                for i in range(first, last):
                    # Calculate offset from the start of the layer
                    offset = i - first
                  
                    # Save top element
                    temp = matrix[first][i]
                  
                    # Move left to top
                    matrix[first][i] = matrix[last - offset][first]
                    matrix[last - offset][first] = matrix[last][last - offset]
                    matrix[last][last - offset] = matrix[i][last]
                    matrix[i][last] = temp
        for rotation_count in range(4):
            if mat == target:
                return True
            rotate_90_clockwise(mat)
            
        return False