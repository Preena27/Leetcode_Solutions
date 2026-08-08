class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        n1, n2 = len(word1), len(word2)
        w2_idx, ans_len = n2 - 1, 0
        match_cnt, ans = [0] * (n1 + 1), []


        for w1_idx in range(n1 - 1, -1, -1):            # <-- #1)

            match_cnt[w1_idx] = match_cnt[w1_idx + 1]

            if w2_idx == -1: continue

            if word1[w1_idx] == word2[w2_idx]:
                match_cnt[w1_idx]+= 1
                w2_idx -= 1


        for w1_idx in range(n1):                        # <-- #2)

            if ans_len == n2: break

            if word1[w1_idx] == word2[ans_len]: 
                ans.append(w1_idx)
                ans_len+= 1
            
            elif match_cnt[w1_idx + 1] + ans_len >= n2 - 1:
                ans.append(w1_idx)
                ans_len+= 1
                break
    
        if ans_len == n2: return ans

        
        w1_idx = 0 if not ans else ans[-1] + 1          # <-- #3)
        w2_idx = ans_len

        if match_cnt[w1_idx] + w2_idx < n2: return []

        while w2_idx < n2:
            if word1[w1_idx] == word2[w2_idx]:
                ans.append(w1_idx)
                w2_idx += 1
            w1_idx += 1
        
        
        return ans