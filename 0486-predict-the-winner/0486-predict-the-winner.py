class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def score(l, r):
            if l == r:
                return nums[l]
            pick_left = nums[l] - score(l + 1, r)
            pick_right = nums[r] - score(l, r - 1)
            return max(pick_left, pick_right)

        return score(0, len(nums) - 1) >= 0
