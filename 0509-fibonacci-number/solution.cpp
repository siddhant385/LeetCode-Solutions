class Solution {
public:
    int sum = 0;
    int fib(int n) {
        if (n<=1){
            return n;
        }
        return fib(n-1)+fib(n-2);
    }
};