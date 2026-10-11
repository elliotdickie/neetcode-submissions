class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A = nums2
            B = nums1
        total = len(A) + len(B)
        half = total//2
        l=0
        r=len(A)-1
        while True:
            i = l+(r-l)//2
            j = half - i -2

            if i >= 0: Aleft = A[i]
            else: Aleft = float("-infinity")
            if i+1 < len(A): Aright = A[i+1]
            else: Aright=float("infinity")
            if j >= 0: Bleft = B[j]
            else: Bleft = float("-infinity")
            if j+1 < len(B): Bright = B[j+1]
            else: Bright = float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright,Bright)
            elif Aleft > Bright:
                r=i-1
            else:
                l=i+1
