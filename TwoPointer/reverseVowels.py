class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        vowels = set('aeiouAEIOU')
        s = list(s)
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        s = ''.join(s)
        return s


myString = input()
obj = Solution()
res = obj.reverseVowels(myString)
print(res)
