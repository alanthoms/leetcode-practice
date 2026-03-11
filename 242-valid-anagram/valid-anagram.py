class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for i,x in enumerate(s):
            count1[x] = count1.get(x, 0) + 1

        for j,y in enumerate(t):
            count2[y] = count2.get(y, 0) + 1

        return count1 == count2
        