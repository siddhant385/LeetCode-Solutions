class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // first we will sort the vector
        sort(nums.begin(),nums.end());
        // looping through 1 to n and if any number is missing cout that
        for(int i=0;i<nums.size();i++){
            if(i != nums[i]){
                return i;
            }
        }
        return nums.size();
        
    }
};