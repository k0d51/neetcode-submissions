class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums2: 
                return [nums2[diff], i]
            else: nums2.update({nums[i] : i})