class Solution:
    def maxArea(self, heights: list[int]) -> int:
        res = 0

        for i, a in enumerate(heights):
            h = a
            for j in range(i+1, len(heights)):
                w = j - i
                if heights[j] < a:
                    h = heights[j]
                else:
                    h = a
                if w*h > res:
                    res = w*h
        
        return res
                