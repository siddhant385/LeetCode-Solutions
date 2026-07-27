class Solution {
public:
    int reverse(int x) {
        long long rev = 0;
        while (x!=0){
            int digit = x%10;
            x = x /10;
            if (rev <= INT_MAX/10 and rev >= INT_MIN/10){
                rev = (rev *10) +digit;
            }else{
                return 0;
            }
        }
        return (rev);
    }
};