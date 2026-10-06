import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s_map = {}
        for c in s1:
            if c in s_map: s_map[c]+=1
            else: s_map[c] = 1
        total = len(s1)
        l=0
        for r in range(len(s2)):
            if s2[r] not in s_map:
                while l < r:
                    s_map[s2[l]] +=1
                    l+=1
                    total +=1
                l=r+1
            else:
                s_map[s2[r]] -=1
                total -=1
                while s_map[s2[r]] < 0:
                    s_map[s2[l]]+=1
                    l+=1
                    total+=1
                if total == 0: return True
        return False