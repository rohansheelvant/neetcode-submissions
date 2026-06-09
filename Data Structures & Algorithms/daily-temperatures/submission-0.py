class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        op = [0 for _ in temperatures]
        stack = []

        for index, val in enumerate(temperatures):
            print(stack)
            if stack == []:
                stack.append((val, index))
            else:
                if val <= stack[-1][0]:
                    stack.append((val, index))
                else:
                    ele = stack[-1]
                    while(ele[0] < val):
                        stack.pop()
                        op[ele[1]] = index - ele[1]

                        if stack == []:
                            break
                        
                        ele = stack[-1]
                    stack.append((val, index))
                    
        return op



