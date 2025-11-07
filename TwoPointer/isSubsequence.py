class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


sub_seq = input()
total_seq = input()
obj = Solution()
ans = obj.isSubsequence(sub_seq, total_seq)
print(ans)
