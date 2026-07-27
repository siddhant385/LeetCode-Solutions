class Solution {
public:
    bool check(vector<int>& nums) {
        int cnt = 0;
        for (int i=0;i<nums.size();i++){
            if (i == nums.size()-1){
                if(nums[0]<nums[i]){
                    cnt ++;
                }
            }
            else if(nums[i]>nums[i+1]){
                cnt ++;
            }
        }
        if (cnt <=1){
            return true;
        }else{
            return false;
        }
        
    }
};