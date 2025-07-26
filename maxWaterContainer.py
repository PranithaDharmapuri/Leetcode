from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        left, right = 0, 1
        while left < len(height)-1:
            j = right
            width = 1
            for i in range(j, len(height)):
                side = min(height[left], height[right])
                max_area = side*(width)
                area.append(max_area)
                width += 1
                if right < len(height)-1:
                    right += 1
            left += 1
            right = left+1

        max_water = max(area)
        return max_water


height = list(map(int, input().split(',')))
obj = Solution()
result = obj.maxArea(height)
print(result)
