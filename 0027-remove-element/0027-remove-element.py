class Solution(object):
    def removeElement(self, nums, val):
        s=0
        for f in range(len(nums)):
            if nums[f]!=val:
                nums[s]=nums[f]
                s+=1
        return s
        