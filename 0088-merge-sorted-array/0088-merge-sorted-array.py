class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:


        del nums1[m:]

        nums1.extend(nums2[:n])
        nums1.sort()