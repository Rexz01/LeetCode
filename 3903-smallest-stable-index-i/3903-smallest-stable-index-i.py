class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
       prefix=[0]*len(nums)
       suffix=[0]*len(nums)
       prefix[0] = nums[0]
       for i in range(1,len(nums)):
        prefix[i]=max(prefix[i-1],nums[i])
       suffix[(len(nums)-1)] = nums[len(nums)-1]
       for i in range(len(nums)-2, -1,-1):
        suffix[i] = min(suffix[i+1], nums[i])
       for i in range (len(nums)):
           if prefix[i]-suffix[i]<=k:
            return i
       return -1
        
 
        