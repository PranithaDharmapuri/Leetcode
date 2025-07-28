from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        minValue = min(nums)
        maxValue = max(nums)
        missedValues = []
        if minValue == maxValue:
            if minValue == 1:
                missedValues.append(minValue+1)
            elif maxValue > 1:
                for i in range(1, maxValue):
                    missedValues.append(i)
        else:
            for i in range(minValue, maxValue+1):
                if i not in nums:
                    missedValues.append(i)
                elif nums.count(i) > 1:
                    continue

        return missedValues


myList = list(map(int, input().split(',')))
obj = Solution()
res = obj.findDisappearedNumbers(myList)
print(res)
