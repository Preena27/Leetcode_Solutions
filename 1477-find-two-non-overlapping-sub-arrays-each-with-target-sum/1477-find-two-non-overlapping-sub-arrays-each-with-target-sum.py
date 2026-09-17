class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # best[i] stores the minimum length of a valid target subarray ending at or before index i
        best = [float('inf')] * n
        
        left = 0
        current_sum = 0
        ans = float('inf')
        min_len = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if current_sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # Valid subarray found
            if current_sum == target:
                length = right - left + 1
                
                # Check if a non-overlapping valid subarray exists before `left`
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])
                
                min_len = min(min_len, length)
            
            # Store the smallest length seen up to index `right`
            best[right] = min_len
            
        return ans if ans != float('inf') else -1