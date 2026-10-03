class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre=0
        mini=0
        maxi=nums[0]
        for i in range(len(nums)):
            pre+=nums[i]
            maxi = max(maxi,pre-mini)
            mini=min(mini,pre)
        return maxi
        