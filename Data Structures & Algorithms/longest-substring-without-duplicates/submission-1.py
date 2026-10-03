class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        chars = set()
        l = 0
        chars.add(s[l])
        r = 0
        max_len = 1
        while r < len(s)-1:
            r+=1
            while l < r and s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
            max_len = max(max_len,r-l+1)
        return max_len

            