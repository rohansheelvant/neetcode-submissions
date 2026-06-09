class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = bin(n)
        return str(temp[2:]).count('1')
        