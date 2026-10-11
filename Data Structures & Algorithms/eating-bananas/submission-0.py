class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = -1
        while l <= r:
            m = l + (r-l)//2
            time = 0
            for pile in piles:
                time += -(pile//-m)
            if time > h:
                l = m+1
            else:
                res = m
                r=m-1
        return res