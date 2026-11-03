class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0:
            return False
        
        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            else:
                if not s[l].isalnum():
                    l+=1
                else:
                    r-=1
        return True