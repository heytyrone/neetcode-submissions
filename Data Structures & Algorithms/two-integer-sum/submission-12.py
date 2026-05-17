class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            diff = target-val
            if diff in nums and i != nums.index(diff):
                return sorted([i, nums.index(diff)])
