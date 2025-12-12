class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        # add array
        nums3.sort()
        # sort not good
        length = len(nums3)
        print(length)
        if length % 2 == 0:
            # if its an even amount
            mid = length / 2
            print(mid)
            mid = int(mid)
            median = nums3[mid - 1] + nums3[mid]
            median = median / 2
            print("hello")
            return median
        elif length % 2 != 0:
            mid = length // 2
            median = nums3[mid]
            print("nooo")
            return median
        return 1
