class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five == 0:
                    return False
                five -=1
                ten +=1
            else:
                if ten < 1:
                    s = 0
                    while s < 15:
                        if five < 1:
                            return False
                        five -= 1
                        s+=5
                else:
                    if five <1:
                        return False
                    five -=1
                    ten -=1
        
        return True

        