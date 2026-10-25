class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for n in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n, c in count.items():
            freq[c].append(n)

        ans = []
        for j in range(len(freq) - 1, 0, -1):
            for i in freq[j]:
                ans.append(i)
                if len(ans) == k:
                    return ans