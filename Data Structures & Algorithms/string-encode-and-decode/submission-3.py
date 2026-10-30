class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i             #Get the number(how long the string is) add our # dilimiter and add our string
        return res

    def decode(self, s: str) -> List[str]:
        
        res, i = [], 0          #Res will be our final list and i will be a pointer 
        
        while i < len(s):       #while i is still in bounds
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
            
        return res