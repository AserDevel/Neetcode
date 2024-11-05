class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
    
        for n in nums:
            for i in range(0, len(subsets)):
                subsetCopy = subsets[i].copy()
                subsetCopy.append(n)
                subsets.append(subsetCopy)
        
        return subsets
                