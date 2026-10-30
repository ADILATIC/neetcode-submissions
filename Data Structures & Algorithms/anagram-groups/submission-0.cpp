class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string,vector<string>> A;          //Declare a map of with the key as a string and value as vector of string
        vector<vector<string>> res;     //Declare a vector of a vector of str
        
        for(string s : strs){       //Iterate through the vector of strs
            string sorted = s;      //Store the strs into a string variable sorted
            sort(sorted.begin(),sorted.end());  //Sort the str
            A[sorted].push_back(s);
        }

        for(auto x : A){        //Now add to the the vector
            res.push_back(x.second);
        }

        return res;
    }
};
