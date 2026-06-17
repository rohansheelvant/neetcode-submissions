class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        len_hand = len(hand)
        hand = sorted(hand)

        if len_hand % groupSize != 0:
            return False

        no_groups = len(hand) // groupSize

        groups = [[] for i in range(no_groups)]

        for val in hand:
            group_found = False
            for group in groups:
                if group == []:
                    group.append(val)
                    group_found = True
                    break
                elif len(group) < groupSize and group[-1] + 1 == val:
                    group.append(val)
                    group_found = True
                    break

            if not group_found:
                print(val, groups)
                return False
        print(groups)
        return True                    
                



        