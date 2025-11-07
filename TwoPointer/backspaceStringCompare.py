class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s)-1
        j = len(t)-1
        myS = []
        myT = []
        while i > 0:
            if s[i] == '#':
                i -= 2
                myS.append(s[i])
            else:
                myS.append(s[i])
                i -= 1
        while j > 0:
            if t[j] == '#':
                j -= 2
                myT.append(t[j])
            else:
                myT.append(t[j])
                j -= 1
        if myS == myT:
            return True


str1 = input("enter the string 1: ")
str2 = input("enter the string 2: ")
obj = Solution()
res = obj.backspaceCompare(str1, str2)
print(res)
