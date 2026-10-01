class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        tdict = {}
        for i in range(len(strs)):
            t = [0] * 26
            for j in range(len(strs[i])):
                t[alphabet.index(strs[i][j])] += 1
            if tuple(t) in tdict: tdict[tuple(t)] += [strs[i]]
            else: tdict.update({tuple(t): [strs[i]]})
        return list(tdict.values())