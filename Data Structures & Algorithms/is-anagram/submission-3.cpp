class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        map<char,int> S;
        map<char,int> T;

        for(int i = 0; i <= s.length(); i++){
            S[s[i]] = S[s[i]]+1;
            T[t[i]] = T[t[i]] +1;
        }

        return S == T;

    }
};
