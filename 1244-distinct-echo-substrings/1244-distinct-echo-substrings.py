class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        subs = set()

        for i in range(len(text)):
            for j in range(i+1, len(text)):
                if(text[i:j] == text[j:j+len(text[i:j])]):
                    subs.add(text[i:j])
        return len(subs)
        