class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        count = []
        for i in nums:
            for j in count:
                if i == j: return True
            count.append(i)
        return False