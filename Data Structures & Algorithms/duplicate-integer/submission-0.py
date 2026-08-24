class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for num in nums:
            a.add(num)
        return len(nums) != len(a)