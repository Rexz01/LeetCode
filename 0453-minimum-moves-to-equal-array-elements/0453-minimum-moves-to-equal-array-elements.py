class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        count = 0

        for num in nums:
            count += num - minimum

        return count