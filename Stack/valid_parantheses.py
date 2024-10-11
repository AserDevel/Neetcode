class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                opened.append(c)
            elif len(opened) == 0:
                return False
            elif c == ')':
                if opened[len(opened)-1] == '(':
                    del opened[len(opened)-1]
                else: return False
            
            elif c == '}':
                if opened[len(opened)-1] == '{':
                    del opened[len(opened)-1]
                else: return False

            else:
                if opened[len(opened)-1] == '[':
                    del opened[len(opened)-1]
                else: return False

        if len(opened) != 0: return False
        else: return True