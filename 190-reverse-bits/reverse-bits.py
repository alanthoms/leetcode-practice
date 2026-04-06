class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1      # make space
            res |= (n & 1)      # add last bit of n
            n >>= 1             # shift n right
        return res