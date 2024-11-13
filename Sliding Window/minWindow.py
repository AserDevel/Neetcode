class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        matches = 0
        s_count = {}
        t_count = {}
        for k in t: t_count[k] = 1 + t_count.get(k, 0)
        
        l = 0
        for r in range(len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            if s_count[s[r]] == t_count.get(s[r], 0):
                matches += 1
            while matches == len(t_count.keys()) and l <= r:
                tmp = s[l:r + 1]
                if len(res) == 0 or len(res) > len(tmp):
                    res = tmp
                s_count[s[l]] -= 1
                if s_count[s[l]] < t_count.get(s[l], 0):
                    matches -= 1
                l += 1

        return res