class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > 1:
                return n
        
        return -1