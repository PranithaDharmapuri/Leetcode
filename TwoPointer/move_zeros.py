from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> int:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k = k+1
        return nums


obj = Solution()
ans = obj.moveZeroes(nums=[0, 1, 0, 3, 12])
print(ans)
