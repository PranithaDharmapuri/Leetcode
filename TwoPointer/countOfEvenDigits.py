from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            strListLenth = len(str(nums[i]))
            if (strListLenth % 2) == 0:
                count += 1
        return count


numList = list(map(int, input().split()))
obj = Solution()
ans = obj.findNumbers(numList)
print(ans)
