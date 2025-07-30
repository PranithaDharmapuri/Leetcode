from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missing = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                missing.append(i)
        return missing


myList = list(map(int, input().split(' ')))
obj = Solution()
res = obj.findDisappearedNumbers(myList)
print(res)
