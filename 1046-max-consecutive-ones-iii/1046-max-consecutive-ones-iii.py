class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        dist = 0

        for r in range(len(nums)):
            if(nums[r] == 0):
                k -= 1

            if(k < 0):
                if(nums[l] == 0):
                    k += 1
                l += 1
            dist = max(dist, r-l+1)
        return dist