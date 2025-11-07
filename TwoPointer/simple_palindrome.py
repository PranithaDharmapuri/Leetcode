class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = len(s)-1
        left = 0

        while left < right:
            while left < right and not s[left].isalnum():
                left = left+1
            while left < right and not s[right].isalnum():
                right = right-1
            if s[left].lower() != s[right].lower():
                return False
            left = left+1
            right = right-1
        return True


s = "A man, a plan, a canal: anama"

sol = Solution()
print(sol.isPalindrome(s))
