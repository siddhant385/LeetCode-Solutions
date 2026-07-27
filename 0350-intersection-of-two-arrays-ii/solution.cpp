class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector <int> sarr;
        vector <int> barr;
        vector <int> iarr;
        if (nums1.size() <= nums2.size()){
            sarr = nums1;
            barr = nums2;
        }else{
            sarr = nums2;
            barr = nums1;
        }
        for (int i=0;i<sarr.size();i++){
            int num = barr.size();
            int j=0;
            while (num >0){
                if (sarr[i] == barr[j]){
                    iarr.push_back(sarr[i]);
                    barr.erase(barr.begin()+j);
                    break;
                }
                num--;
                j++;
            }
        }return iarr;
        
    }
};