from functools import cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            left = piles[i] - dp(i + 1, j)
            right = piles[j] - dp(i, j - 1)
            return max(left, right)
        
        return dp(0, len(piles) - 1) > 0
