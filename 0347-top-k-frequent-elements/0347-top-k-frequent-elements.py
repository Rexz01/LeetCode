class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        ans = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        out = []
        for key in ans:
            out.append(key[0])

        res = []
        for i in range(k):
            res.append(out[i])

        return res