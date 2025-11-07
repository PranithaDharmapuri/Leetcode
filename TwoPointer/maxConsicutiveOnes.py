from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                maxCount = max(count, maxCount)
                count = 0
            else:
                count += 1
                if i == len(nums)-1:
                    maxCount = max(count, maxCount)
        return maxCount


myList = list(map(int, input().split()))
obj = Solution()
ans = obj.findMaxConsecutiveOnes(myList)
print(ans)
