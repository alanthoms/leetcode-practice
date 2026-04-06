class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = bin(n)[2:].zfill(32)
        print(reverse)
        reverse = reverse[::-1]
        print(reverse)
        return int(reverse, 2)