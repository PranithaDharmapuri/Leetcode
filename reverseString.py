from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> int:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


obj = Solution()
ans = obj.reverseString(s=[1, 23, 45, 67])
print(ans)
