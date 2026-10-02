class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ch=''.join(sorted(s))
        ch1=''.join(sorted(t))
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if ch[i]!=ch1[i]:
                return False
        return True



        