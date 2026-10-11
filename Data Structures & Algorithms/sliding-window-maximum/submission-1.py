class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while dq and dq[-1] < nums[r]:
                dq.pop()
            dq.append(nums[r])
            if r-l+1 == k:
                res.append(dq[0])
                if nums[l] == dq[0]: dq.popleft()
                l+=1
        
        return res