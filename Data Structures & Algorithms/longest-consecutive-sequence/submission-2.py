class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = 1
        streak = 0
        
        sortedList = sorted(nums)
        if len(sortedList) == 0:
            return 0
        elif len(sortedList) == 1:
            return 1
        prev = sortedList[0]


        
        for i in sortedList[1:]:
            
            if  i - prev == 1:
                count += 1
                prev = i
            elif i - prev == 0:
                prev = i
            else:
                prev = i
                count = 1
            
            if streak < count:
                streak = count


        return streak