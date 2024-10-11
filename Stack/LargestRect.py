class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        output = 0
        
        for i in range(len(heights)):
            h = heights[i]
            w = 1
            maxA = h*w
            for j in range(i+1, len(heights)):
                w += 1
                if heights[j] < h:
                    h = heights[j]
                if h*w > maxA:
                    maxA = h*w

            if maxA > output:
                output = maxA
        
        return output
