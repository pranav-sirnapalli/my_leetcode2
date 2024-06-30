class Solution:
    def reverseWords(self, s: str) -> str:
        req_val = s.split()
        result = ''
        length = len(req_val) - 1

        while(length>=0):
            result = result + req_val[length] + " "
            length -= 1
        
        return result[:-1]

        
