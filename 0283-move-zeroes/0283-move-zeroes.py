class Solution(object):
    def moveZeroes(self, nums):
        s=0
        for f in range(len(nums)):
            if nums[f]!=0:
                temp=nums[f]
                nums[f]=nums[s]
                nums[s]=temp
                
                s+=1

        return nums
        