class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp=0
        res=0
        li = ['a','e','i','o','u']
        for i in range(k):
            if s[i] in li:
                res+=1
        temp=res
        for i in range(k,len(s)): 
            if s[i] in li:
                res+=1
            if s[i-k] in li:
                res-=1
            temp= max(temp,res)
        return temp