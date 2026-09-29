class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        substr_maxlen = 0
        for i in range(len(s)):
            if s[i] not in substr: 
                substr += s[i]
                substr_maxlen = max(substr_maxlen, len(substr))
            else: 
                substr = substr[substr.find(s[i])+1:] + s[i]
        return substr_maxlen
            
        