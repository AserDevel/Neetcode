class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strlist = []
        while len(strs) != 0:
            templist = [strs[0]]
            for s in range(1, len(strs)):
                if isAnagram(strs[0], strs[0], strs[s]):
                    templist.append(strs[s])
            strlist.append(templist)
            for x in templist:
                strs.remove(x)
        print(strlist)
        return strlist


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


#test
strs = ["x","x"]

Solution.groupAnagrams(strs, strs)