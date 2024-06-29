class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if(len(word1) == 0 and len(word2) != 0):
            return word2
        if(len(word1) != 0 and len(word2) == 0):
            return word1
        new_word = ""
        l1 = len(word1)
        l2 = len(word2)
        i = j = 0
        while(i<l1 and j<l2):
            new_word = new_word+word1[i]+word2[j]
            i += 1
            j += 1
        
        if(i >= l1 and j < l2):
            while(j < l2):
                new_word = new_word + word2[j]
                j += 1
        
        if(i < l1 and j >= l2):
            while(i < l1):
                new_word = new_word + word1[i]
                i += 1
        
        return new_word
        

        