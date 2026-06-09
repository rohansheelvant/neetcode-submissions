class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            if val not in ["+", "-", "*", "/"]:
                stack.append(int(val))
            else:
                val1 = stack[-2]
                val2 = stack[-1]
                stack.pop()
                stack.pop()

                if val == "+":
                    stack.append(val1+val2)
                elif val == "-":
                    stack.append(val1-val2)
                elif val == "*":
                    stack.append(val1*val2)
                elif val == "/":
                    stack.append(int(val1/val2))
                
                #print(stack)
                
        return int(stack[0])
                
        