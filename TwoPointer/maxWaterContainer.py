from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left < right:
            width = right-left
            size = min(height[left], height[right])
            curr_area = width*size
            max_area = max(curr_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


height = list(map(int, input().split(',')))
obj = Solution()
result = obj.maxArea(height)
print(result)
