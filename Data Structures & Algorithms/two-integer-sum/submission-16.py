class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        j = 0
        seen = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            #seen.append(i)
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return
          
            