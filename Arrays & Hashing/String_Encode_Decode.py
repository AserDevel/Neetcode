class Solution:

    def encode(self, strs: list[str]) -> str:
        output = ""
        for s in strs:
            s_encoded = s.encode("utf-8", "backslashreplace")
            output += str(s_encoded)
        output = output[2:len(output)-1]
        print(output)
        
        return output
    
    def decode(self, s: str) -> list[str]:
        if s == "": return []
        strlist = s.split("'b'")
        print(strlist)
        
        return strlist

test = ["neet","code","b","love","you"]
Solution.decode(0, Solution.encode(0, test))