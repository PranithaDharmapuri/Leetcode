class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        str = ' '.join(reversed_words)
        return str


obj = Solution()
ans = obj.reverseWords(s="let's have some fun")
print(ans)
