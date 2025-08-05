class Solution(object):
    def validPalindrome(self, s):  # "abca"
        i, j, count = 0, len(s)-1, 0
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if s[i+1] == s[j]:
                    i += 2
                    j -= 1
                elif s[i] == s[j-1]:
                    i += 1
                    j -= 2
                else:
                    return False
            if i >= j:
                return True


myString = input("Enter the string: ")
obj = Solution()
res = obj.validPalindrome(myString)
print(res)
