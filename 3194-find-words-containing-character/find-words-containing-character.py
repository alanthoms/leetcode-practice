class Solution:
    def findWordsContaining(self, words, x):
        r = []
        for i,y in enumerate(words):
            for j in y:
                if j == x:
                    r.append(i)
                    break
        return r
            
        