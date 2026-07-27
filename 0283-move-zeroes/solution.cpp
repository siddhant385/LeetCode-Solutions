class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int indx=0;
        int cnt = 0;
        while (cnt <nums.size() ){
            if (nums[indx]==0){
                nums.insert(nums.end(),0);
                nums.erase(nums.begin()+indx);
                cnt++;
            }else{
                cnt++;
                indx++;
            }
        }
        

        }
        
};