class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        pow = x * self.myPow(x, abs(n)-1)
        if n > 0:
            return pow
        return 1/pow
    
print(Solution().myPow(2.00, -200))