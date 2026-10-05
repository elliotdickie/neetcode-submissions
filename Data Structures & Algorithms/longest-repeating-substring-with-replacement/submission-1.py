class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #need to track the most common character
        #keep hashtable of characters and their frequency
        #keep array tracking most common character and its frequency
        #update hash table, and if equal, mcc whenever frequency is updated
        #k_remainder = k-mcc
        if s == "": return 0
        mcc = [s[0],1]
        c_map = {s[0]:1}
        l = 0
        r = 0
        max_len = 1
        while r < len(s)-1:
            r+=1
            if s[r] in c_map: c_map[s[r]]+=1
            else: c_map[s[r]] =1
            if s[r] == mcc[0]: mcc[1] += 1
            elif c_map[s[r]] > mcc[1]:
                mcc[0] = s[r]
                mcc[1] = c_map[s[r]]
            while r-l+1 - mcc[1] > k:
                c_map[s[l]] -=1
                mcc[0] = max(c_map,key=c_map.get)
                mcc[1] = c_map[mcc[0]]
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len
