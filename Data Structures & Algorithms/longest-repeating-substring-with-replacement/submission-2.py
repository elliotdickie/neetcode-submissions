class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_set = set(s)
        for c in char_set:
            l=0
            freq=0
            for r in range(len(s)):
                if s[r] == c: freq+=1
                while r-l+1 - freq > k:
                    if s[l] == c: freq-=1
                    l+=1
                max_len = max(r-l+1,max_len)
        return max_len
