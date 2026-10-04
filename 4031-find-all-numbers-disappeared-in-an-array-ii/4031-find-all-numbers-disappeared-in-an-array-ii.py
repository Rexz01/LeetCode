class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        s = set()

        for i in range(len(nums)):
            s.add(nums[i])

        li = []

        for i in range(lower, upper + 1):
            if i not in s:
                li.append(i)

        ans = []
        help = []

        if len(li) == 0:
            return ans

        x = li[0]

        for i in range(1, len(li)):
            if li[i] == li[i - 1] + 1:
                continue
            else:
                help.append([x, li[i - 1]])
                x = li[i]

        help.append([x, li[-1]])

        return help