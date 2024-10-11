class Solution:
    def trap(self, height: list[int]) -> int:
        tallest = 0
        res = 0

        for i in range(len(height)):
            if height[i] > height[tallest]:
                tallest = i

        peak = height[0]
        steps = 0
        terrain = 0
        for i in range(1, tallest+1):
            if height[i] >= peak:
                res += steps*peak - terrain
                peak = height[i]
                steps = 0
                terrain = 0
            else:
                terrain += height[i]
                steps += 1
        
        peak = height[len(height)-1]
        steps = 0
        terrain = 0
        for i in range(len(height)-2, tallest-1, -1):
            if height[i] >= peak:
                res += steps*peak - terrain
                peak = height[i]
                steps = 0
                terrain = 0
            else:
                terrain += height[i]
                steps += 1

        return res