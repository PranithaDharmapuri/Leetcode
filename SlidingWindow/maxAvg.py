from typing import List


class Solution:
    def maxAvg(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        maxSum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum+nums[i]-nums[i-k]

            if window_sum > maxSum:
                maxSum = window_sum

        return maxSum/k


obj = Solution()
myList = list(map(int, input("Enter the list: ").split(",")))
subArraySize = int(input("Enter the window size: "))
result = obj.maxAvg(myList, subArraySize)
print(result)
