class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        j = 0

        for i in gain:
            val = i + res[j]
            res.append(val)
            j += 1

        return max(res)
        