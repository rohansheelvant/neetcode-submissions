from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        len_hand = len(hand)
        hand = sorted(hand)

        groups_left = len_hand // groupSize
        if len_hand % groupSize != 0:
            return False
        
        element_left = defaultdict(int)

        for ele in hand:
            if element_left[ele] > 0:
                element_left[ele] -= 1
                continue
        
            groups_left -= 1
            for val in range(ele+1, ele+groupSize):
                element_left[val] += 1
            if groups_left < 0:
                return False
        
        return True