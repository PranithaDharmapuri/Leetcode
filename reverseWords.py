class Reverse:
    def reverseWords(self, s: str) -> str:
        words = list(s.split())
        myList = []

        for word in words:
            left, right = 0, len(word)-1
            word = list(word)
            while left <= right:
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
            word = ''.join(word)
            myList.append(word)
            myString = ' '.join(myList)
        return myString


string = input()
obj = Reverse()
ans = obj.reverseWords(string)
print(ans)

"""class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = [word[::-1] for word in words]
        str = ' '.join(reversed_words)
        return str


obj = Solution()
ans = obj.reverseWords(s="let's have some fun")
print(ans)"""
