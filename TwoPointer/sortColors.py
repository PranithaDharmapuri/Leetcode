from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros, ones, twos = 0, 0, 0
        for num in range(len(nums)):
            if nums[num] == 0:
                zeros += 1
            elif nums[num] == 1:
                ones += 1
            elif nums[num] == 2:
                twos += 1
        for i in range(zeros):
            nums[i] = 0
        for j in range(zeros, zeros+ones):
            nums[j] = 1
        for k in range(zeros+ones, len(nums)):
            nums[k] = 2
        print(nums)


nums = list(map(int, input().split()))
obj = Solution()
res = obj.sortColors(nums)
