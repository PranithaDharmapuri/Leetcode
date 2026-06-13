class Solution(object):
    def isPalindrome(self, s):
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower() 
        l=0
        r=len(res)-1
        for i in range(len(res)):
            if res[l]!=res[r]:
                return False
            l+=1
            r-=1

        return True

        
        