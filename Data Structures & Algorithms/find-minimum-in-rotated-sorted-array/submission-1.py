class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallestSoFar = 1001
        l = 0
        r=len(nums)-1
        while l <= r:
            m = l+(r-l)//2
            if nums[l] <= nums[m]:
                smallestSoFar = min(smallestSoFar,nums[l])
                l = m+1
            else:
                smallestSoFar = min(smallestSoFar,nums[m])
                r=m-1
        return smallestSoFar