class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        ans = []
        prev = lower - 1
        nums.sort()

        for i in range(len(nums)):
            num = nums[i]

            if num < lower:
                continue

            if num > upper:
                break

            if num - prev >= 2:
                ans.append([prev + 1, num - 1])

            prev = num

        if upper + 1 - prev >= 2:
            ans.append([prev + 1, upper])

        return ans