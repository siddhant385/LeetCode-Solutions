class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority = nums.size()/2;
        map <int,int> arr;
        for(int num: nums){
            arr[num]++;
        }
        int max = 0;
        int numb = 0;
        for(auto& [num,count]:arr){
            if (count>max){
                numb = num;
                max = count;
            }
        }return numb;
        
    }
};