class Solution {
public:
    vector <int> numl={1,4,5,9,10,40,50,90,100,400,500,900,1000};
    vector <string> stringl={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
    string intToRoman(int num) {
        int indx=12;
        string res = "";
        while(indx>=0){
            int div = num/numl[indx];
            for (int i=0;i<div;i++){
                res+=stringl[indx];
            }
            num = num%numl[indx];
            indx--;
        }
        return res;

        
    };
};