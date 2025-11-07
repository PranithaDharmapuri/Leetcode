class Solution(object):
    def minSubArrayLen(self, target, nums):
        sorted_nums = sorted(nums)


myArray = list(map(int, input().split(' ')))
target_val = int(input("Enter target: "))
obj = Solution()
res = obj.minSubArrayLen(target_val, myArray)
