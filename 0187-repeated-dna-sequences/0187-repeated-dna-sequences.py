class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # to hold final list and seen once list
        res = set()
        seen = set()

        # We need to make sure there is always 10 characters
        for i in range(len(s)-9):
            val = s[i: i+10]
            if(val in seen):
                res.add(val)
            seen.add(val)
        return list(res)

        