class Solution(object):
    def removeDuplicates(self, nums):
        s=0
        for f in range(1,len(nums)):
            if nums[s]!=nums[f]:
                s+=1
                nums[s]=nums[f]

        return s+1