import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max = 0

        for p in piles:
            if p > max:
                max = p

        k = math.ceil(max / (h - len(piles) + 1))  
        
        x = h + 1
        while x > h:
            x = 0
            for p in piles:
                x += math.ceil(p / k)
            if x > h:
                k += 1

        return k