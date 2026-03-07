class Solution:
    def minFlips(self, s: str) -> int:
        k = len(s)
        s = s + s

        flag1, flag2 = '0', '1'
        st1, st2 = '0', '1'

        left = 0
        ch1 = ch2 = 0
        result = float('inf')

        for right in range(len(s)):

            if s[right] != flag1:
                ch1 += 1
            if s[right] != flag2:
                ch2 += 1

            flag1 = '1' if flag1 == '0' else '0'
            flag2 = '1' if flag2 == '0' else '0'

            if right - left + 1 > k:

                if s[left] != st1:
                    ch1 -= 1
                if s[left] != st2:
                    ch2 -= 1

                left += 1

                st1 = '1' if st1 == '0' else '0'
                st2 = '1' if st2 == '0' else '0'

            if right - left + 1 == k:
                result = min(result, min(ch1, ch2))

        return result