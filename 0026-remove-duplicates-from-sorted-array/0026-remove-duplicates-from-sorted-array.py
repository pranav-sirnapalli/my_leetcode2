class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tot = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[tot] = nums[i]
                tot += 1
        return tot