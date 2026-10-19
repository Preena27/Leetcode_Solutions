class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        result = [i for i, v in enumerate(nums) if v == target]
        return result