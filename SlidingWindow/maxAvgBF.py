from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) > 1:
            left = 0
            right = k-1
        elif len(nums) == 1:
            left, right = 0, 0
        sum = 0
        maxSum = 0
        for i in range(left, k):
            sum += nums[i]
        while right < len(nums)-1:
            sum -= nums[left]
            left += 1
            right += 1
            sum += nums[right]
            maxSum = max(maxSum, sum)

        ans = maxSum/k
        return ans


obj = Solution()
myList = list(map(int, input("Enter the List: ").split(" ")))
subArraySize = int(input("Enter the sub Array size: "))
result = obj.findMaxAverage(myList, subArraySize)
print(result)
