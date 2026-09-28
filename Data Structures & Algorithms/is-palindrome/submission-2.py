class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        for i in range(1,len(s)):
            if s[i-1] == s[-i]: continue
            else: return False
        return True