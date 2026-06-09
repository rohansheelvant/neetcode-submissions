class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start_index = 0
        end_index = len(nums)-1

        start = 0
        end = len(nums)-1

        t1 = 0
        t2 = 0

        while(start<=end):
            t1 += nums[start]
            t2 += nums[end]
            print(t1, t2, start, end)
            if (t1<=0 and t2>0) or (t1<=0 and t2<=0 and t1<t2):
                start_index = start+1
                t1 = 0
                start+=1
            elif (t2<=0 and t1>0) or (t1<=0 and t2<=0 and t1>=t2):
                end_index = end-1
                t2 = 0
                end-=1
            else:
                start+=1
                end-=1
        
        print(start_index, end_index)

        if(end_index<start_index):
            return max(nums)
        
        return sum(nums[start_index:end_index+1])


        