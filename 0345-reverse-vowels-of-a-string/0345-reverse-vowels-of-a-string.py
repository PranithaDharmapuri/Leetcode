class Solution(object):
    def reverseVowels(self, s):
        l=0
        r=len(s)-1
        lst=[]
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for ch in s:
            lst.append(ch)
        while l<=r:
            if lst[l] in vowels and lst[r] in vowels:
                temp=s[l]
                lst[l]=lst[r]
                lst[r]=temp
                r-=1
                l+=1
            elif lst[r] not in vowels:
                r-=1
            elif lst[l] not in vowels:
                l+=1
        s="".join(lst)
        return s