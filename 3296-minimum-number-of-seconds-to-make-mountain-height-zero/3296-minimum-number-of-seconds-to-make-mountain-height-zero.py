class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(T):
            total = 0
            for w in workerTimes:
                x = int((-1 + math.isqrt(1 + 8*T//w)) // 2)
                total += x
            return total >= mountainHeight

        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left