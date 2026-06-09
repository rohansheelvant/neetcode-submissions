class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = 0
        max_len = 0

        for r in range(0, len(s)):
            val_r = s[r]
            if val_r in hm:
                hm[val_r] += 1
            else:
                hm[val_r] = 1
            
            while(r-l+1 - max(hm.values()) > k):
                val_l = s[l]
                hm[val_l] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len

        