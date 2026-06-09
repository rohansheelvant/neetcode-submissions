class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        extra = ""
        combined = ""
        for word in strs:
            combined += word
            start = "1"
            for i in range(0, len(word)):
                start += "0"
            extra += start
        
        return combined+extra+"#"+str(len(combined))

    def decode(self, s: str) -> List[str]:
        if "#" not in s:
            return []
        combined_len, s = int(s.split("#")[-1]), "#".join(s.split("#")[:-1])
        combined, extra = s[:combined_len], s[combined_len:]
        op = []
        curr = None
        index = 0
        for val in extra:
            if val == "1":
                if curr != None:
                    op.append(curr)
                curr = ""
            else:
                if curr == None:
                    curr = ""
                curr += combined[index]
                index += 1
            
        op.append(curr)
        return op