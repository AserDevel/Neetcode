class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        for i in range(n):
            bit = 1
            count = 0
            while i & bit:
                count += 1
                bit = bit << 1
            res.append(res[i] - count + 1)
        
        return res