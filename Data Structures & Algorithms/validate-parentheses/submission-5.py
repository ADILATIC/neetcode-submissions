class Solution:
    def isValid(self, s: str) -> bool:
        stack = []          
        mapp = { '}' : '{' , ')' : '(' , ']' : '[' }  #Store the map with options

        for i in range (len(s)):    #iterate through the stroing
            if s[i] in mapp:    
                if stack and mapp[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False  
            else:
                stack.append(s[i])
            
        if stack:
            return False
        else:
            return True