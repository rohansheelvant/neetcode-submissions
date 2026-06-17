from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        len_hand = len(hand)
        no_of_grps = int(len_hand//groupSize)

        if len_hand % groupSize != 0:
            return False
        
        item_counter = defaultdict(int)
        for val in hand:
            item_counter[val] += 1
        min_val, max_val = min(hand), max(hand)

        start_rem = no_of_grps

        for i in range(min_val, max_val+1):
            if start_rem != 0:
                count = item_counter[i]
                item_counter[i] = 0
                start_rem -= count
                if start_rem < 0:
                    print('a')
                    return False
                for cnt in range(count):
                    for j in range(i+1, i+groupSize):
                        if item_counter[j] <= 0:
                            print('b')
                            return False
                        item_counter[j] -= 1
        if start_rem != 0:
            print('c')
            return False
        
        return True



