class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for word in strs:
            key = [0 for _ in range(26)]
            for letter in word:
                key[ord(letter)-97] += 1
            
            key = tuple(key)
            if key in hm:
                hm[key].append(word)
            else:
                hm[key] = [word]
        
        ret = []
        for key, val in hm.items():
            ret.append(val)
        
        return ret
        




        