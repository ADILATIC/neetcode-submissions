class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        result = [[] for i in range(len(nums) + 1)]

        for num in nums:
           freq[num] = 1 + freq.get(num,0)

        for num, c in freq.items():
            result[c].append(num)

        res = []
        for i in range(len(result) -1 ,0 , -1):
            for n in result[i]:
                res.append(n)
                if len(res) == k:
                    return res