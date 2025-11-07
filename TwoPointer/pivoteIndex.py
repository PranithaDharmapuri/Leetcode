class Solution(object):
    def pivotIndex(self, nums):
        left_sum, right_sum = 0, 0
        pivoteIndex = []
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                pivoteIndex.append(i)
        if not pivoteIndex:
            return -1
        else:
            return pivoteIndex[0]

        """total = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if 2 * left_sum + num == total:
                return i
            left_sum += num

        return -1"""


myList = list(map(int, input().split(" ")))
obj = Solution()
res = obj.pivotIndex(myList)
print(res)
