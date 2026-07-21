class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        total_ones = 0  # Total count of '1's in the string
        index = 0
      
        # Initialize variables for tracking consecutive zero segments
        previous_zero_segment = float('-inf')  # Length of previous '0' segment
        max_zero_gain = 0  # Maximum gain from converting zeros to ones
      
        # Process the string by consecutive segments of same characters
        while index < n:
            # Find the end of current segment with same character
            segment_end = index + 1
            while segment_end < n and s[segment_end] == s[index]:
                segment_end += 1
          
            # Calculate current segment length
            current_segment_length = segment_end - index
          
            if s[index] == '1':
                # Add all '1's to the total count
                total_ones += current_segment_length
            else:
                # For '0' segments, track the maximum potential gain
                # by considering trading adjacent zero segments
                max_zero_gain = max(max_zero_gain, 
                                   previous_zero_segment + current_segment_length)
                previous_zero_segment = current_segment_length
          
            # Move to the next segment
            index = segment_end
      
        # Return total ones plus the maximum possible gain from trading zeros
        result = total_ones + max_zero_gain
        return result