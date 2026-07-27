class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        revnum = self.revnum(x)
        if revnum == x:
            return True
    def revnum(self,x):
        #example number = 121
        rev = 0
        while x != 0:
            rem = x % 10 # gives value 1 \\ gives value 2 \\ gives value 1
            rev = rev*10 + rem# gives value 1
            x = x // 10
        print(rev)
        return rev



        