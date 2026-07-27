class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int index =0;
        while (index <nums.size()-1){
            if (nums[index]!=nums[index+1]){
                index++;
            }
            else{
                nums.erase(nums.begin()+(index+1));
            }

        }return nums.size();
    }
};