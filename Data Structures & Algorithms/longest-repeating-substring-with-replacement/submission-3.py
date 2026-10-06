class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        char_map = {}
        max_freq = 0
        l=0
        for r in range(len(s)):
            if s[r] in char_map: char_map[s[r]]+=1
            else: char_map[s[r]]=1
            if char_map[s[r]] > max_freq: max_freq = char_map[s[r]]
            while r-l+1-max_freq > k:
                char_map[s[l]] -=1
                l+=1
            max_len = r-l+1
        return max_len
