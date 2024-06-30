class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)

        return max(0, (max_val-k) - (k+min_val))
        