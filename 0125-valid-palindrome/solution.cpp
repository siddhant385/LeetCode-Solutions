class Solution {
private:
    string cleanstr(string s) {
        string ans = "";
        for (auto ch : s) {
        // if the current character
        // is an alphabet
        if ( isalnum(ch)){ans += ch;}
        else{continue;}}
        return ans;}
public:
    bool isPalindrome(string s) {
        s = cleanstr(s);
        cout << s;
        int n = s.size();
        for (int i=0;i<= n-i-1;i++){
            if (tolower(s[i]) != tolower(s[n-i-1])){
                return false;
            }
        }
        return true;
    }
};