class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for x in bin(n):
            if x == "1":
                res += 1
        return res

        