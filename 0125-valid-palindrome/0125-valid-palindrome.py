class Solution(object):
    def isPalindrome(self, s):
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower()
        s=res

        
        l=0
        r=len(res)-1
        while(l<=r):
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1

        return True

        
        