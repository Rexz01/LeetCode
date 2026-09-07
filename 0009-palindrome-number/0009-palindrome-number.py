class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0:
            return False
        if x == 0 :
            return True
        m=""
        y= x
        while x>0:
            m+=str(x%10)
            x=x//10
        z =int(m)
       
        if z==y:
            return True
        return False
        