class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, int> digitSumMap; // Maps digit sum to the max number with that sum
        int maxSum = -1;

        for (int num : nums) {
            int dsum = getDigitSum(num);

            // If a number with this digit sum exists, check for max sum
            if (digitSumMap.find(dsum) != digitSumMap.end()) {
                maxSum = max(maxSum, digitSumMap[dsum] + num);
            }

            // Store the max number for this digit sum
            digitSumMap[dsum] = max(digitSumMap[dsum], num);
        }

        return maxSum;
    }

private:
    int getDigitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10; // Extract last digit
            n /= 10;       // Remove last digit
        }
        return sum;
    }
};