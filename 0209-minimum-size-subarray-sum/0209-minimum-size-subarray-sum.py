class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        left = 0
        help = 0
        count = float('inf')

        for i in range(len(nums)):

            help += nums[i]

            while help >= target:
                count = min(count, i - left + 1)
                help -= nums[left]
                left += 1

        return 0 if count == float('inf') else count