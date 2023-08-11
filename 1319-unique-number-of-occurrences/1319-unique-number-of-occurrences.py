import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        tot = collections.Counter(arr)
        occ = tot.values()
        return (len(occ) == len(set(occ)))
