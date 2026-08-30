class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        see = set()
        for num in nums:
            if num in see:
                return True
            see.add(num)
        return False
        