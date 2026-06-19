class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapping = { str(i):i for i in range(0,10)}

        int1 = 0
        int2 = 0
        for val in num1:
            int1 = int1*10 + mapping[val]
        
        for val in num2:
            int2 = int2*10 + mapping[val]

        return str(int1*int2)
        