class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(curr: list[int], left: list[int]):
            if len(left) < 1:
                res.append(curr)
                return
            for n in left:
                left_copy = left.copy()
                left_copy.remove(n)
                curr_copy = curr.copy()
                curr_copy.append(n)
                dfs(curr_copy, left_copy)
        
        dfs([], nums)
        return res