class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        help = []

        for i in range(m, len(nums1)):
            help.append(nums1[i])

        del nums1[m:]

        nums1.extend(nums2[:n])
        nums1.sort()