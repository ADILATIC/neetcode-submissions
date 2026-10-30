class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       

        array = []
        for i in range (len(s)):
            if s[i].isalnum():
                array.append(s[i])
            else:
                continue
        j = len(array) - 1;
        print(array)

        if(len(array) == 1):
            return True


        for i in range (len(array)):
            # array = array.lower()
            if(array[i].lower() != array[j].lower()):
                    return False
            j-=1
        return True