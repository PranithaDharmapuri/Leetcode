class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]

        nums.sort()
        
        # s=0
        # for f in range(1,len(nums)):
        #     if nums[f]<nums[s]:
        #         temp=nums[s]
        #         nums[s]=nums[f]
        #         nums[f]=temp
        #         s+=1
        return nums
        