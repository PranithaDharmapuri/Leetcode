# Filename: remove_duplicates.py (or any name you like)

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1 

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


#if __name__ == "__main__":
nums = [1, 1, 2]
sol = Solution() 
k = sol.removeDuplicates(nums)

output_nums = nums[:k] + ["_"] * (len(nums) - k)
print(f"Output: {k}, nums = {output_nums}")
