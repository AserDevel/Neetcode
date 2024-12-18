import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        q = collections.deque() # index dequeue
        l = r = 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:  
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res