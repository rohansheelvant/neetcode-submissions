class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        max_len = 0
        l = 0
        for index in range(0, len(s)):
            val = s[index]
            if val in hm and hm[val] >= l:
                max_len = max(max_len, index-l)
                l = hm[val] + 1
                hm[val] = index
                #print(index, hm, l)

            else:
                hm[val] = index        

        #print(hm, l)
        max_len = max(max_len, len(s)-l)
        return max_len

        
        