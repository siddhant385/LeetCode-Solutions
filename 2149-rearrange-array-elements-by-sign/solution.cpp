class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> post;
        vector<int> neg;
        for(int num: nums){
            if (num>0){
                post.push_back(num);
            }else{
                neg.push_back(num);
            }
        };
        vector<int> res;
        for (int i=0;i<post.size();i++){
            res.push_back(post[i]);
            res.push_back(neg[i]);
            

        };
        return res;
        
    }
};