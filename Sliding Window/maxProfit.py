class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        low, high = prices[0], 0
        for p in prices:
            if p < low:
                low = p
            if p - low > high:
                high = p - low

        return high