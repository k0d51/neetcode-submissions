class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        countt = {}
        for n in s:
            if n not in counts: counts.update({n:1})
            else: counts[n]+=1
        for n in t:
            if n not in countt: countt.update({n:1})
            else: countt[n]+=1
        if countt == counts: return True
        else: return False
