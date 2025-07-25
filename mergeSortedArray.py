from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1.append(nums2[i])
        print(sorted(nums1))


nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
obj = Solution()
ans = obj.merge(nums1, len(nums1), nums2, len(nums2))
