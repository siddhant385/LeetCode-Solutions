class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count,lcount=0;
        for(int i=0;i<nums.size();i++){
            if (nums[i]==0){
                if (count > lcount){
                    lcount = count;
                }
                count =0;
            }else{
                count ++;
            }
        }
        if (count > lcount){
                    lcount = count;
                }
        return lcount;
        
    }
};