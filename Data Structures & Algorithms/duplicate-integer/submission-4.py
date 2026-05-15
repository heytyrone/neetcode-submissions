class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_set = set()
        for item in nums:
            if item in checked_set:
                return True
            checked_set.add(item)
        return False