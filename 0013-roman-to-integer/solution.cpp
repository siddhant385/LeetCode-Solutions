class Solution {
public:
    int romanToInt(string s) {
        map <string,int> mp;
        vector<string> sym = {"I","V","X","L","C","D","M"};
        vector<int> numl = {1,5,10,50,100,500,1000};
        for (int i=0;i<sym.size();i++){
            mp[sym[i]] = numl[i];
        };         
        int size = s.length();
        int num = 0;
        int init = 0;
        while (size>=0){
            if (init <= mp[string(1,s[size])]){
                init = mp[string(1,s[size])];
                num +=mp[string(1,s[size])];
                size--;
            }else{
                num -=mp[string(1,s[size])];
                size--;
            }
            


        }
        return num;
    };
};