class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums2: return [nums2.index(diff), i]
            else: nums2.append(nums[i])