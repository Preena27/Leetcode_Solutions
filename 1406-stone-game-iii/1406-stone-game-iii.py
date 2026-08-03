from functools import cache
from math import inf
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dp(i: int) -> int:
            if i >= len(stoneValue):
                return 0
            best = -inf
            total = 0
            for x in range(3):
                if i + x < len(stoneValue):
                    total += stoneValue[i + x]
                    best = max(best, total - dp(i + x + 1))
            return best

        score = dp(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
