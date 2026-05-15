class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_dict = {}
        for item in nums:
            if item in checked_dict:
                return True
            checked_dict[item] = 1
        return False