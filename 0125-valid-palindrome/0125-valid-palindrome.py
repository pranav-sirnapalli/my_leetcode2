class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_new = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                str_new = str_new + i
        if(str_new == str_new[::-1]):
            return True
        else:
            return False

        