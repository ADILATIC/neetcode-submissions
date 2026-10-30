class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string , vector<string>> map;
        vector<vector<string>> res;

        for(string s : strs){
            string sorted = s;
            sort(sorted.begin(), sorted.end());
            map[sorted].push_back(s);
        }

        for(auto x : map){
            res.push_back(x.second);
        }
        
        return res;
    }
};
