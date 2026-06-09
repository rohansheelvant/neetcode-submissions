class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for val in s:
            if stack and val == stack[-1]:
                stack.pop(-1)
            elif val in mapping:
                stack.append(mapping[val])
            else:
                return False
        
        return stack == []

        