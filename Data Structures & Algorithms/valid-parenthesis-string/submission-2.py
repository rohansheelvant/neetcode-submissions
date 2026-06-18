class Solution:
    def checkValidString(self, s: str) -> bool:
        avlb = [True] * len(s) # True if slot available, False if already paired
        opn = []
        close = []

        for i in range(len(s)):
            if s[i] == "*":
                continue
            elif s[i] == '(':
                opn.append(i)
            elif s[i] == ')':
                if opn:
                    ele = opn.pop()
                    avlb[i] = False
                    avlb[ele] = False
                else:
                    close.append(i)
        
        avlb_index = [i for i in range(len(avlb)) if avlb[i]]
        print(opn, close, avlb_index)

        if opn != []:
            pointer = len(s)-1
            for index_i in opn[::-1]:
                found = False
                while(not found and pointer > index_i):
                    if s[pointer] == "*" and avlb[pointer]:
                        avlb[pointer] = False
                        found = True

                    pointer -= 1   
                if not found:
                    return False
                                     
        if close != []:
            pointer = len(s)-1
            for index_i in close[::-1]:
                found = False
                while pointer >= index_i:
                    pointer -= 1

                while(not found and pointer >= 0):
                    if s[pointer] == "*" and avlb[pointer]:
                        avlb[pointer] = False
                        found = True

                    pointer -= 1  

                if not found:
                    return False
                
        return True 
        
        