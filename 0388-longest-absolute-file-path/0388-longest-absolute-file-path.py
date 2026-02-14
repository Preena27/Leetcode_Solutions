class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        stack = [0]  
        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.replace("\t", "")
            while len(stack) > depth + 1:
                stack.pop()
            if "." in name:  
                max_len = max(max_len, stack[-1] + len(name))
            else:  
                stack.append(stack[-1] + len(name) + 1) 
        return max_len
