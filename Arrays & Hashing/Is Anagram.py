class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = [x for x in s]
        tlist = [x for x in t]
        if len(slist) != len(tlist): return False
        for sc in slist:    
            for tc in tlist:
                if sc == tc:
                    tlist.remove(tc)
                    break
        if len(tlist) == 0: return True 
        else: return False
    
    s = "racecar"
    t = "carrace"
    isAnagram(s,s,t)