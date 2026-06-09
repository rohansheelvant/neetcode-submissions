class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict

        window = len(s1)

        if len(s2) < window:
            return False
        
        track1 = defaultdict(int)
        track2 = defaultdict(int)

        for i in range(window):
            track1[s1[i]] += 1
            track2[s2[i]] += 1

        j = 0
        while(j < len(s2)-window):
            if track1 == track2:
                return True
            
            track2[s2[j]] -= 1
            if track2[s2[j]] == 0:
                del track2[s2[j]]
            
            track2[s2[j+window]] += 1
            
            j += 1
        
        if track1 == track2:
            return True

        return False 


        