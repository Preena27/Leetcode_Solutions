class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        stack = []
        indices.sort(key=lambda i: positions[i])
        for current_index in indices:
            if directions[current_index] == "R":
               
                stack.append(current_index)
            else:
                # Robot moving left: check for collisions with robots moving right
                while stack and healths[current_index] > 0:
                    # Get the rightmost robot moving right
                    top_index = stack.pop()
                  
                    if healths[top_index] > healths[current_index]:
                        # Right-moving robot wins: reduce its health by 1
                        healths[top_index] -= 1
                        healths[current_index] = 0
                       
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        
                        healths[current_index] -= 1
                        healths[top_index] = 0
                      
                    else:
                        
                        healths[current_index] = 0
                        healths[top_index] = 0
        result = [health for health in healths if health > 0]
        return result