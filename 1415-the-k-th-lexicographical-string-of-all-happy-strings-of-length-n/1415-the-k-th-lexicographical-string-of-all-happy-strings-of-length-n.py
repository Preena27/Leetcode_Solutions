class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = [] 
        def backtrack(curr):
            if len(curr) == n:
                res.append(curr)
                return
            for ch in ['a', 'b', 'c']:
                if not curr or curr[-1] != ch:
                    backtrack(curr + ch)
        backtrack("")
        return res[k-1] if k <= len(res) else ""