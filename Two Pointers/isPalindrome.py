import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s)
        r = s[::-1]
        r = r.capitalize()
        s = s.capitalize()

        flag = True
        for c in range(len(s)):
            if s[c] != r[c]:
                flag = False
        
        return flag