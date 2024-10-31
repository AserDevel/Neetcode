class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        s2_count = {}
        for c in s1: s1_count[c] = 1 + s1_count.get(c, 0) 

        l = 0
        for r in range(len(s2)):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            while s1_count.get(s2[r], 0) < s2_count[s2[r]]:
                s2_count[s2[l]] -= 1 
                l += 1
            
            flag = True
            for k in s1_count.keys():
                if s2_count.get(k, 0) != s1_count[k]:
                    flag = False
            if flag: return True
            
        return False