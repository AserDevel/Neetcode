class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        total_combs = [[]]
        for n in nums:
            new_combs = [[n]]
            sm = n
            while sm < target:
                sm += n
                new_combs.append([n] * (sm  // n))
            for i in range(0, len(total_combs)):
                for j in range(0, len(new_combs)):
                    newComb = total_combs[i] + new_combs[j]
                    x = sum(newComb)
                    if x == target:
                        res.append(newComb)
                    elif x < target:
                        total_combs.append(newComb)
                    else:
                        break
        return res