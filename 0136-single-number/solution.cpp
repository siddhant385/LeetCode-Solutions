class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int xorn = 0;
        for(int i=0;i<nums.size();i++){
            xorn = xorn^nums[i];
        }
        return xorn;
        
    }
};