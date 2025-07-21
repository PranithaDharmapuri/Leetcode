class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return 0
        k=0
        for i in range(0,len(nums)):
            nums[i]=nums[i]*nums[i]
            nums[k]=nums[i]
            k=k+1
        nums.sort()
        return nums

nums=[-2,0,2,5,4]
obj=Solution()

ans=obj.sortedSquares(nums)
print(ans)