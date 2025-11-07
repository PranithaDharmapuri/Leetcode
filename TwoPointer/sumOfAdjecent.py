class Solution:
    def SumOfAdjacent(self, nums):
        i, j, sum = 0, 1, 0
        while (j < len(nums)):
            sum = sum+nums[i]+nums[j]
            i += 2
            j += 2
            if j >= len(nums):
                sum = sum+nums[i]
        return sum


myList = list(map(int, input("Enter the rray of elements: ").split(" ")))

obj = Solution()
result = obj.SumOfAdjacent(myList)
print(result)
