class Solution:
    def numSteps(self, s: str) -> int:
        steps, carry = 0, 0
        n = len(s)
        for i in range(n - 1, 0, -1):
            if int(s[i]) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps + carry
