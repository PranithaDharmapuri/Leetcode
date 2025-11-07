from typing import List


class Solution:
    # nums=[1 1 1], k=2;  o/p:[1,1]=1+1=2 and [1,1]=1+1=2 fimal o/p=2 subarrays
    def subarraySum(self, nums: List[int], k: int) -> int:
        i, j, sum, count = 0, 1, 0, 0
        while j < len(nums):
            if i < j:
                sum += nums[i]+nums[j]
                i += 1
                j += 1
                if sum == k:
                    count += 1
                    sum = 0
            if nums[i] == k:
                sum += nums[i]
                count += 1
                sum = 0
            elif nums[j] == k:
                sum += nums[j]
                count += 1
                sum = 0
        return count


myList = list(map(int, input("Enter the array of elements: ").split(" ")))
target = int(input("enter the target: "))
obj = Solution()
res = obj.subarraySum(myList, target)
print(res)
