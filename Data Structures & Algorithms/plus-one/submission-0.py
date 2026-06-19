class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for digit in digits:
            string += str(digit)
        val = int(string)
        val += 1
        string = str(val)
        return [i for i in string]
        