
class Solution {
public:
    bool isPalindrome(int x) {
        int dup =x;
        int rev = 0;
        while (dup!=0){
            int digit = dup%10;
            dup = dup/10;
            if (rev > INT_MAX/10 || rev < INT_MIN/10){
                return false;
            };
            rev = rev*10 + digit;
        }
        if (rev != x || rev <0){
            return false;
        }
        return true;
        
    }
};