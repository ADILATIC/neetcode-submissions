class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map < int, int> prevMap;
        for( int i = 0; i < nums.size(); i++){
            prevMap[nums[i]] = i;
        }

        for(int i =0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(prevMap.count(diff) && prevMap[diff]!= i)

                return{i, prevMap[diff]};
        }
        return {};
    }
};
