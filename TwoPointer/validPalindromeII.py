class Solution(object):
    def validPalindrome(self, s):  # "abca"
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                skipI, skipJ = s[i+1:j+1], s[i:j]
                return (skipI == skipJ[::-1] or skipJ == skipJ[::-1])
            i, j = i+1, j-1
        return True


myString = input("Enter the string: ")
obj = Solution()
res = obj.validPalindrome(myString)
print(res)
