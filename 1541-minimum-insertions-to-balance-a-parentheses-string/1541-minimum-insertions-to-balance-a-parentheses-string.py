class Solution:
    def minInsertions(self, s: str) -> int:
        insertions_needed = 0
        unmatched_left_parens = 0

        index = 0
        string_length = len(s)

        while index < string_length:
            if s[index] == '(':
                unmatched_left_parens += 1
            else:
                if index < string_length - 1 and s[index + 1] == ')':
                    index += 1
                else:
                    insertions_needed += 1

                if unmatched_left_parens == 0:
                    insertions_needed += 1
                else:
                    unmatched_left_parens -= 1

            index += 1

        insertions_needed += unmatched_left_parens * 2

        return insertions_needed