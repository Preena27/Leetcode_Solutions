class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0

        for position, char in enumerate(s, 1):
            reverse_alphabet_position = 26 - (ord(char) - ord('a'))
            total_sum += position * reverse_alphabet_position

        return total_sum