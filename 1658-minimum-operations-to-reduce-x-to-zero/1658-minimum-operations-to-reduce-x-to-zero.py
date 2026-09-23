class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        prf,sfx = [*accumulate(nums, initial=0)], [*accumulate(nums[::-1], initial=0)]
        return  min((
            j + idx  for j in range((bisect_left(prf, x) +1) %(len(prf) +1))  # early exit
            if  x == ((val:= prf[j]) + sfx[idx:= bisect_left(sfx, x-val)])
        ), default=-1)
            
        