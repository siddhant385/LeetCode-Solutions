class Solution {
private:
    string cleanstr(string s) {
        string ans = "";
        for (auto ch : s) {
        if (isalnum(ch)){ans += ch;}
        }
        return ans;}
public:
    bool isPalindrome(string s) {
        s = cleanstr(s);
        int n = s.size();
        for (int i=0;i<= n-i-1;i++){
            if (tolower(s[i]) != tolower(s[n-i-1])){
                return false;
            }
        }
        return true;
    }
};