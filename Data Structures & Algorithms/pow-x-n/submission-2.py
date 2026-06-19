class Solution:
    def myPow(self, x: float, n: int) -> float:
        op = x
        if n > 0:
            for _ in range(n-1):
                op = op*x
        else:
            for _ in range(-n+1):
                op = op/x
        if n == 0:
            return 1
        return op
        