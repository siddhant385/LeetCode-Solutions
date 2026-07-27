class Solution {
public:
    int findClosest(int x, int y, int z) {
        int step1 = abs(z-x);
        int step2 = abs(z-y);
        if (step1<step2){
            return 1;
        }else if(step2< step1){
            return 2;
        }else{
            return 0;
        }
        
    }
};