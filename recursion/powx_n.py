class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        else:
            half = self.myPow(x, (n - 1) // 2)
            return x * half * half

res = Solution().myPow(34.00515, -3)

# ✅ Two ways to round/format
print(round(res, 5))