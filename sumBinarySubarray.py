class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        l, r, curr_sum, count = 0, 0, 0, 0
        if goal < 0:
            return 0
        while r < len(nums):
            curr_sum = sum(nums[l:r+1])
            while curr_sum > goal:
                l += 1
                r += 1
                if r >= len(nums):
                    r-+1

            if curr_sum == goal:
                count += 1
            r += 1
            if r > len(nums):
                r -= 1
        return count


myList = list(map(int, input("Enter the binary list: ").split(" ")))
target_sum = int(input("Enter the goal sum value: "))
obj = Solution()
res = obj.numSubarraysWithSum(myList, target_sum)
print(res)
