class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        if(n == 1):
            return float(nums[0])
        
        i = 0
        sum = 0
        for i in range(k):
            sum += nums[i]
        
        max_avg = sum / k

        for i in range(k, n):
            sum += nums[i]
            sum -= nums[i-k]
            max_avg = max(max_avg, sum/k)
        
        return max_avg