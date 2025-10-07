class Solution:
    def findWordsContaining(self, words, x):
        r = []
        for i,word in enumerate(words):
            if x in word:
                r.append(i)
        return r
            
        