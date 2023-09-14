class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        n = len(text)

        l = r = ''

        for i in range(n):
            l = l + text[i]
            r = text[n-i-1] + r

        
            if(l == r):
                res += 1
                l = ''
                r = ''
        
        return res
        
