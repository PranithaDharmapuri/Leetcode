from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''myList = []
        for num in nums:
            if num not in myList:
                myList.append(num)
            else:
                return num'''
        mySet = set()
        for i in nums:
            if i in mySet:
                return i
            else:
                mySet.add(i)


numsList = list(map(int, input().split(" ")))
obj = Solution()
res = obj.findDuplicate(numsList)
print(res)
