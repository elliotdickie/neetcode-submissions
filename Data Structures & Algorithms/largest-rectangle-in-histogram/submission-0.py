class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #stores biggest element
        max_area = 0
        for i in range(len(heights)):
            left = i
            while stack and heights[stack[-1]] >= heights[i]:
                area = heights[stack[-1]] * (i-stack[-1])
                max_area = max(area,max_area)
                left = stack[-1]
                stack.pop()
            heights[left] = heights[i]
            stack.append(left)
        while stack:
            area = heights[stack[-1]] * (len(heights)-stack[-1])
            max_area = max(area,max_area)
            stack.pop()
        return max_area

            

