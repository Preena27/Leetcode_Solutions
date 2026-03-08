class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result_bits = []
        for i in range(n):
            if nums[i][i] == '0':
                result_bits.append('1')
            else:
                result_bits.append('0')
        return ''.join(result_bits)