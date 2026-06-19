class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while(n!=1):
            next_val = 0 
            for digit in str(n):
                next_val += int(digit)**2
            n = next_val
            if n in seen:
                return False
            seen.add(n)

        return True
        